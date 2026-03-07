<script setup>
import { ref, computed, onMounted } from 'vue'
import { getVendas, updateVenda, deleteVenda } from '../services/api'
import StatCard from '../components/StatCard.vue'
import { DollarSign, ShoppingBag, TrendingUp, Calendar, CheckSquare, Square, Trash2, Edit, X } from 'lucide-vue-next'

const vendas = ref([])
const loading = ref(true)
const error = ref(null)

const periodoAtual = ref('hoje') // hoje, semana, mes


onMounted(async () => {
  await carregarVendas()
})

const carregarVendas = async () => {
  loading.value = true
  error.value = null
  try {
    const data = await getVendas()
    vendas.value = data
    console.log(`Vendas carregadas: ${data.length} registros`)
  } catch (err) {
    error.value = 'Falha ao carregar vendas. Verifique a conexão com o servidor.'
    console.error(err)
  } finally {
    loading.value = false
  }
}

const showEditModal = ref(false)
const editForm = ref({
  id: null,
  nome: '',
  valor: 0,
  quantidade: 1,
  observacoes: '',
  data: '',
  lancado: false
})

const editarVenda = (venda) => {
  editForm.value = { ...venda }
  showEditModal.value = true
}

const deletarVenda = async (id) => {
  if (!window.confirm('Tem certeza que deseja apagar esta venda?')) return
  
  try {
    await deleteVenda(id)
    vendas.value = vendas.value.filter(v => v.id !== id)
  } catch (err) {
    console.error('Erro ao deletar:', err)
    alert('Falha ao deletar a venda.')
  }
}

const salvarEdicao = async () => {
  try {
    const data = await updateVenda(editForm.value.id, editForm.value)
    const index = vendas.value.findIndex(v => v.id === data.id)
    if (index !== -1) {
      vendas.value[index] = data
    }
    showEditModal.value = false
  } catch (err) {
    console.error('Erro ao salvar:', err)
    alert('Falha ao salvar as alterações.')
  }
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
}

const formatDate = (dateString) => {
  return new Intl.DateTimeFormat('pt-BR', { dateStyle: 'short', timeStyle: 'short' }).format(new Date(dateString))
}

// Filtro
const vendasFiltradas = computed(() => {
  const agora = new Date()
  return vendas.value.filter(v => {
    const dataVenda = new Date(v.data)
    
    if (periodoAtual.value === 'hoje') {
      return dataVenda.toDateString() === agora.toDateString()
    }
    
    if (periodoAtual.value === 'semana') {
      // Últimos 7 dias (janela deslizante incluindo hoje)
      const dataLimite = new Date(agora)
      dataLimite.setDate(agora.getDate() - 7)
      dataLimite.setHours(0,0,0,0)
      return dataVenda >= dataLimite
    }
    
    if (periodoAtual.value === 'mes') {
      // Últimos 30 dias (janela deslizante incluindo hoje)
      const dataLimite = new Date(agora)
      dataLimite.setDate(agora.getDate() - 30)
      dataLimite.setHours(0,0,0,0)
      return dataVenda >= dataLimite
    }
    
    return true
  })
})

const totalArrecadado = computed(() => {
  return vendasFiltradas.value.reduce((acc, curr) => acc + (curr.valor * curr.quantidade), 0)
})

const qtdVendas = computed(() => {
  // A quantidade de vendas no histórico deve ser o total de registros (transações únicas)
  return vendasFiltradas.value.length
})

const ticketMedio = computed(() => {
  if (qtdVendas.value === 0) return 0
  return totalArrecadado.value / qtdVendas.value
})

const toggleLancado = async (venda) => {
  const novoStatus = !venda.lancado;
  venda.lancado = novoStatus; // optimistic update
  
  try {
    const payload = { ...venda, lancado: novoStatus };
    await updateVenda(venda.id, payload);
  } catch (err) {
    venda.lancado = !novoStatus; // revert on fail
    console.error('API Error updating lancado:', err);
    alert('Não foi possivel atualizar o status de lançamento no servidor.');
  }
}
</script>

<template>
  <div class="p-6 md:p-10 max-w-7xl mx-auto space-y-8">
    <header class="flex flex-col md:flex-row md:justify-between md:items-end gap-4">
      <div>
        <h2 class="text-3xl font-heading text-text-primary font-bold">Visão Geral</h2>
        <p class="text-text-secondary mt-1">Acompanhe suas vendas e marque os lançamentos realizados.</p>
      </div>

      <!-- Filtro de Datas -->
      <div class="inline-flex bg-surface rounded-lg p-1 border border-gray-200 shadow-sm">
        <button 
          v-for="p in ['hoje', 'semana', 'mes']" :key="p"
          @click="periodoAtual = p"
          :class="[
            'px-6 py-2 rounded-md text-sm font-medium transition-colors capitalize',
            periodoAtual === p ? 'bg-primary text-white shadow' : 'text-text-secondary hover:bg-gray-50'
          ]"
        >
          {{ p }}
        </button>
      </div>
    </header>

    <div v-if="loading" class="flex justify-center items-center py-20">
      <div class="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary"></div>
    </div>
    
    <div v-else-if="error" class="bg-error/10 border-error/20 border text-error p-4 rounded-lg">
      {{ error }}
      <button @click="carregarVendas" class="ml-4 underline font-medium">Tentar novamente</button>
    </div>

    <template v-else>
      <!-- Cards de Métricas -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <StatCard 
          title="Total Arrecadado" 
          :value="formatCurrency(totalArrecadado)" 
          :icon="DollarSign"
          iconColor="text-success"
          iconBg="bg-success/20"
        />
        <StatCard 
          title="Quantidade de Vendas" 
          :value="qtdVendas.toString()" 
          :icon="ShoppingBag"
        />
        <StatCard 
          title="Ticket Médio" 
          :value="formatCurrency(ticketMedio)" 
          :icon="TrendingUp"
        />
      </div>

      <!-- Tabela de Vendas -->
      <div class="bg-surface rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 class="text-lg font-bold text-text-primary flex items-center gap-2">
            <Calendar class="w-5 h-5 text-primary" />
            Vendas do Período
          </h3>
          <span class="text-sm text-text-secondary bg-gray-100 px-3 py-1 rounded-full">
            {{ vendasFiltradas.length }} registros
          </span>
        </div>
        
        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-gray-50/50 text-text-secondary text-sm">
                <th class="p-4 font-medium text-center w-16">Status</th>
                
                <th class="p-4 font-medium text-left">Produto</th>
                
                <th class="p-4 font-medium text-left">Data</th>
                
                <th class="p-4 font-medium text-left">Unitário</th>
                
                <th class="p-4 font-medium text-left">Qtd</th>
                
                <th class="p-4 font-medium text-left">Total</th>
                
                <th class="p-4 font-medium text-right">Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="vendasFiltradas.length === 0">
                <td colspan="7" class="p-8 text-center text-text-secondary">
                  Nenhuma venda encontrada para este período.
                </td>
              </tr>
              <tr 
                v-for="venda in vendasFiltradas" 
                :key="venda.id"
                :class="[
                  'border-t border-gray-50 transition-colors',
                  venda.lancado ? 'bg-success/5' : 'hover:bg-gray-50/50'
                ]"
              >
                <!-- Checkbox Lançado -->
                <td class="p-4 text-center">
                  <button 
                    @click="toggleLancado(venda)"
                    class="focus:outline-none transition-transform active:scale-95"
                  >
                    <CheckSquare v-if="venda.lancado" class="w-6 h-6 text-success mx-auto" stroke-width="2.5" />
                    <Square v-else class="w-6 h-6 text-gray-300 hover:text-primary transition-colors mx-auto" />
                  </button>
                </td>
                
                <td class="p-4">
                  <p class="font-medium text-text-primary" :class="{'line-through text-text-secondary': venda.lancado}">
                    {{ venda.nome }}
                  </p>
                  <p v-if="venda.observacoes" class="text-xs text-text-secondary mt-0.5 truncate max-w-xs" :class="{'line-through': venda.lancado}">
                    {{ venda.observacoes }}
                  </p>
                </td>
                <td class="p-4 text-sm text-text-secondary" :class="{'line-through': venda.lancado}">
                  {{ formatDate(venda.data) }}
                </td>
                <td class="p-4 text-text-primary" :class="{'line-through text-text-secondary': venda.lancado}">
                  {{ formatCurrency(venda.valor) }}
                </td>
                <td class="p-4 text-text-primary" :class="{'line-through text-text-secondary': venda.lancado}">
                  {{ venda.quantidade }}
                </td>
                <td class="p-4 font-bold text-primary" :class="{'line-through text-text-secondary font-medium': venda.lancado}">
                  {{ formatCurrency(venda.valor * venda.quantidade) }}
                </td>
                <td class="p-4 text-right">
                  <div class="flex justify-end gap-2">
                    <button 
                      @click="editarVenda(venda)"
                      class="p-2 text-primary hover:bg-primary/10 rounded-lg transition-colors"
                      title="Editar"
                    >
                      <Edit class="w-5 h-5" />
                    </button>
                    <button 
                      @click="deletarVenda(venda.id)"
                      class="p-2 text-error hover:bg-error/10 rounded-lg transition-colors"
                      title="Deletar"
                    >
                      <Trash2 class="w-5 h-5" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </template>

    <!-- Modal de Edição -->
    <div v-if="showEditModal" class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm">
      <div class="bg-surface w-full max-w-lg rounded-2xl shadow-2xl border border-gray-100 overflow-hidden animate-in fade-in zoom-in duration-200">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50/50">
          <h3 class="text-xl font-bold text-text-primary">Editar Venda</h3>
          <button @click="showEditModal = false" class="text-text-secondary hover:text-primary p-1">
            <X class="w-6 h-6" />
          </button>
        </div>
        
        <form @submit.prevent="salvarEdicao" class="p-6 space-y-4">
          <div>
            <label class="block text-sm font-medium text-text-secondary mb-1">Produto</label>
            <input 
              v-model="editForm.nome" type="text" required
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all"
            />
          </div>
          
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label class="block text-sm font-medium text-text-secondary mb-1">Valor Unitário</label>
              <div class="relative">
                <span class="absolute left-4 top-1/2 -translate-y-1/2 text-text-secondary">R$</span>
                <input 
                  v-model.number="editForm.valor" type="number" step="0.01" required
                  class="w-full pl-10 pr-4 py-2 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all"
                />
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-text-secondary mb-1">Quantidade</label>
              <input 
                v-model.number="editForm.quantidade" type="number" required min="1"
                class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all"
              />
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-medium text-text-secondary mb-1">Observações</label>
            <textarea 
              v-model="editForm.observacoes" rows="3"
              class="w-full px-4 py-2 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all resize-none"
            ></textarea>
          </div>
          
          <div class="pt-4 flex gap-3">
            <button 
              type="button" @click="showEditModal = false"
              class="flex-1 px-6 py-3 rounded-xl border border-gray-200 font-bold text-text-secondary hover:bg-gray-50 transition-all"
            >
              Cancelar
            </button>
            <button 
              type="submit"
              class="flex-[2] px-6 py-3 rounded-xl bg-primary text-white font-bold shadow-lg shadow-primary/20 hover:scale-[1.02] active:scale-95 transition-all"
            >
              Salvar Alterações
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Trash2, CalendarHeart, Pencil, X, Save } from 'lucide-vue-next'
import { getSalesToday, deleteSale, updateSale } from '../services/api'

const router = useRouter()
const goBack = () => router.push('/')

const sales = ref([])
const isLoading = ref(true)
const salesTotal = computed(() => sales.value.reduce((acc, sale) => acc + sale.valor, 0))

const formatCurrency = (value) => {
  return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)
}

const loadSales = async () => {
  isLoading.value = true
  try {
    sales.value = await getSalesToday()
  } catch (error) {
    console.error(error)
  } finally {
    isLoading.value = false
  }
}

const removeSale = async (id) => {
  try {
    await deleteSale(id)
    sales.value = sales.value.filter(s => s.id !== id)
  } catch (error) {
    alert("Erro ao deletar a venda.")
  }
}

const editingSale = ref(null)
const isUpdating = ref(false)
const editForm = ref({ nome: '', valor: '', quantidade: 1, observacoes: '' })

const startEdit = (sale) => {
  editingSale.value = sale.id
  editForm.value = { ...sale }
}

const cancelEdit = () => {
  editingSale.value = null
}

const saveEdit = async () => {
  if (!editForm.value.nome || !editForm.value.valor) return
  isUpdating.value = true
  try {
    let valorStr = editForm.value.valor.toString().replace(',', '.')
    let valorLimpo = parseFloat(valorStr)
    editForm.value.valor = valorLimpo
    
    // Maintain the correct API structure
    const dataToSend = {
      nome: editForm.value.nome,
      valor: editForm.value.valor,
      quantidade: parseInt(editForm.value.quantidade),
      observacoes: editForm.value.observacoes,
      data: editForm.value.data
    }

    const updated = await updateSale(editingSale.value, dataToSend)
    const index = sales.value.findIndex(s => s.id === editingSale.value)
    if (index !== -1) sales.value[index] = updated
    cancelEdit()
  } catch (error) {
    alert("Erro ao salvar edição.")
  } finally {
    isUpdating.value = false
  }
}

onMounted(() => {
  loadSales()
})
</script>

<template>
  <div class="w-full h-full flex flex-col max-h-screen">
    <!-- Header -->
    <header class="flex items-center justify-between mb-6 shrink-0 pt-4">
      <div class="flex items-center gap-4">
        <button @click="goBack" class="p-2 rounded-full hover:bg-black/5 transition-colors text-text-primary">
          <ArrowLeft class="w-6 h-6" />
        </button>
        <div>
          <h1 class="text-2xl font-heading font-bold text-text-primary">Histórico</h1>
          <p class="text-sm font-body text-text-secondary">Vendas de hoje</p>
        </div>
      </div>
      
      <div class="text-right glass-card px-4 py-2 rounded-2xl flex items-center gap-2">
        <CalendarHeart class="w-4 h-4 text-primary" />
        <span class="font-bold text-primary">{{ formatCurrency(salesTotal) }}</span>
      </div>
    </header>

    <!-- Content Area (Scrollable) -->
    <div class="flex-1 overflow-y-auto pb-10 space-y-4 px-1 rounded-3xl no-scrollbar">
      
      <div v-if="isLoading" class="flex justify-center items-center h-40 text-text-secondary">
        <div class="w-6 h-6 border-2 border-primary border-t-transparent rounded-full animate-spin"></div>
        <span class="ml-3 font-medium">Carregando amor...</span>
      </div>

      <div v-else-if="sales.length === 0" class="flex flex-col justify-center items-center h-40 text-text-secondary/70">
        <CalendarHeart class="w-12 h-12 mb-2 text-primary/30" />
        <p class="font-medium text-lg">Nenhuma venda hoje.</p>
        <p class="text-sm">Os registros aparecerão aqui :)</p>
      </div>

      <!-- Sales List -->
      <transition-group name="slide-fade" tag="div" class="space-y-4">
        <div 
          v-for="sale in sales" 
          :key="sale.id"
          class="bg-white rounded-3xl p-5 shadow-sm border border-secondary/20 flex items-center justify-between hover:shadow-md transition-shadow relative overflow-hidden group"
        >
          <!-- Accent Line -->
          <div class="absolute left-0 top-0 bottom-0 w-1.5 bg-primary/40 rounded-l-3xl"></div>

          <div class="pl-2">
            <h3 class="font-bold text-lg text-text-primary mb-0.5">{{ sale.nome }}</h3>
            <div class="flex items-center gap-3 text-sm text-text-secondary">
              <span class="font-semibold text-primary/80">{{ formatCurrency(sale.valor) }}</span>
              <span class="w-1 h-1 rounded-full bg-secondary"></span>
              <span>Qtd: {{ sale.quantidade }}</span>
            </div>
            <p v-if="sale.observacoes" class="text-xs text-text-secondary/70 mt-1 italic">
              "{{ sale.observacoes }}"
            </p>
          </div>

          <div class="flex items-center">
            <button 
              @click="startEdit(sale)"
              class="p-2.5 hover:bg-primary/10 text-text-secondary hover:text-primary rounded-xl transition-colors opacity-60 group-hover:opacity-100"
            >
              <Pencil class="w-5 h-5" />
            </button>
            <button 
              @click="removeSale(sale.id)"
              class="p-2.5 hover:bg-error/10 text-text-secondary hover:text-error rounded-xl transition-colors opacity-60 group-hover:opacity-100"
            >
              <Trash2 class="w-5 h-5" />
            </button>
          </div>
        </div>
      </transition-group>

    </div>

    <!-- Edit Modal -->
    <div v-if="editingSale" class="absolute inset-0 z-50 flex items-center justify-center p-4 bg-black/40 backdrop-blur-sm">
      <div class="glass-card w-full max-w-sm p-6 relative">
        <button @click="cancelEdit" class="absolute top-4 right-4 text-text-secondary hover:text-text-primary transition-colors">
          <X class="w-6 h-6" />
        </button>
        <h2 class="text-xl font-body font-bold text-primary mb-5">Editar Venda</h2>
        
        <form @submit.prevent="saveEdit" class="space-y-4">
          <input v-model="editForm.nome" type="text" placeholder="Nome do Produto" required class="w-full px-4 py-3 bg-white/50 border border-primary/20 rounded-xl focus:ring-2 focus:ring-primary outline-none text-text-primary">
          <div class="flex gap-4">
            <input v-model="editForm.valor" type="text" inputmode="decimal" placeholder="Valor" required class="w-2/3 px-4 py-3 bg-white/50 border border-primary/20 rounded-xl focus:ring-2 focus:ring-primary outline-none text-text-primary">
            <input v-model="editForm.quantidade" type="number" min="1" placeholder="Qtd" required class="w-1/3 px-4 py-3 bg-white/50 border border-primary/20 rounded-xl focus:ring-2 focus:ring-primary outline-none text-text-primary">
          </div>
          <input v-model="editForm.observacoes" type="text" placeholder="Observações..." class="w-full px-4 py-3 bg-white/50 border border-primary/20 rounded-xl focus:ring-2 focus:ring-primary outline-none text-text-primary">
          
          <button type="submit" :disabled="isUpdating" class="w-full mt-2 py-4 bg-primary text-white rounded-full font-medium shadow-md hover:bg-primary/90 transition-all flex justify-center items-center gap-2">
            <Save class="w-5 h-5" /> {{ isUpdating ? 'Salvando...' : 'Salvar Alterações' }}
          </button>
        </form>
      </div>
    </div>

  </div>
</template>

<style scoped>
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Gift, DollarSign, Package, MessageSquare, Heart, CheckCircle, Clock } from 'lucide-vue-next'
import { createSale, getSalesToday } from '../services/api'

const router = useRouter()
const goBack = () => router.push('/')

const form = ref({
  nome: '',
  valor: '',
  quantidade: 1,
  observacoes: ''
})

const isLoading = ref(false)
const errorMessage = ref('')
const successMessage = ref('')

const submitSale = async () => {
  if (!form.value.nome || !form.value.valor) {
    errorMessage.value = "Por favor, preencha o nome e o valor!"
    return
  }
  
  errorMessage.value = ''
  isLoading.value = true
  
  try {
    const valorLimpo = parseFloat(form.value.valor.toString().replace(',', '.'))
    
    if (isNaN(valorLimpo)) throw new Error("Valor inválido")

    await createSale({
      nome: form.value.nome,
      valor: valorLimpo,
      quantidade: parseInt(form.value.quantidade),
      observacoes: form.value.observacoes,
      data: new Date().toISOString()
    })
    
    successMessage.value = "Venda registrada com sucesso! 🤍"
    
    setTimeout(() => {
      router.push('/history')
    }, 1500)
    
  } catch (error) {
    errorMessage.value = "Erro ao conectar com o servidor."
  } finally {
    isLoading.value = false
  }
}

const recentProducts = ref([])

const loadRecentProducts = async () => {
  try {
    const sales = await getSalesToday()
    const uniqueMap = new Map()
    for (const sale of [...sales].reverse()) {
      const key = sale.nome.toLowerCase().trim()
      if (!uniqueMap.has(key)) {
        uniqueMap.set(key, { nome: sale.nome, valor: sale.valor })
      }
    }
    recentProducts.value = Array.from(uniqueMap.values()).slice(0, 10)
  } catch (error) {
    console.error("Erro ao carregar produtos recentes:", error)
  }
}

const selectRecentProduct = (product) => {
  form.value.nome = product.nome
  // Replace dot with comma for inputmode="decimal" consistency if desired, or just pass as string
  form.value.valor = product.valor.toString().replace('.', ',')
}

onMounted(() => {
  loadRecentProducts()
})
</script>

<template>
  <div class="w-full h-full flex flex-col">
    <!-- Header -->
    <header class="flex items-center gap-4 mb-6">
      <button @click="goBack" class="p-2 rounded-full hover:bg-black/5 transition-colors text-text-primary">
        <ArrowLeft class="w-6 h-6" />
      </button>
      <h1 class="text-2xl font-heading font-bold text-text-primary">Novo Registro</h1>
    </header>

    <!-- Glass Form Card -->
    <div class="glass-card p-6 flex flex-col space-y-6">
      
      <div class="text-center mb-2">
        <h2 class="text-xl font-body font-semibold text-primary">O que estamos vendendo, amor?</h2>
      </div>

      <!-- Recent Products Mini Cards -->
      <div v-if="recentProducts.length > 0" class="flex flex-col space-y-3 -mt-2">
        <div class="flex items-center gap-2 text-primary/70 mb-1">
          <Clock class="w-4 h-4" />
          <h3 class="text-xs font-body font-bold uppercase tracking-wider">Produtos Recentes</h3>
        </div>
        
        <div class="flex overflow-x-auto gap-3 pb-3 no-scrollbar -mx-2 px-2">
          <button 
            v-for="product in recentProducts" 
            :key="product.nome"
            @click="selectRecentProduct(product)"
            type="button"
            class="flex-shrink-0 flex items-center gap-3 bg-white/50 border border-primary/10 hover:bg-white hover:shadow-md hover:border-primary/30 rounded-full pl-1.5 pr-4 py-1.5 transition-all group focus:outline-none focus:ring-2 focus:ring-primary/40 transform active:scale-95 max-w-[220px]"
          >
            <div class="w-9 h-9 rounded-full bg-gradient-to-br from-primary/20 to-primary/5 flex items-center justify-center text-primary shadow-inner shrink-0 scale-95 group-hover:scale-105 transition-transform">
              <Package class="w-4 h-4" />
            </div>
            <div class="flex flex-col justify-center text-left">
              <span class="font-bold text-text-primary group-hover:text-primary transition-colors text-sm truncate max-w-[120px]" :title="product.nome">{{ product.nome }}</span>
              <span class="text-text-secondary/80 text-[11px] font-medium">{{ new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(product.valor) }}</span>
            </div>
          </button>
        </div>
      </div>

      <form @submit.prevent="submitSale" class="space-y-4">
        <!-- Input Nome -->
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-primary">
            <Gift class="w-5 h-5" />
          </div>
          <input 
            v-model="form.nome" 
            type="text" 
            placeholder="Nome do Produto"
            required
            class="w-full pl-12 pr-4 py-3 bg-white/50 border border-primary/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-primary focus:bg-white transition-all text-text-primary placeholder:text-text-secondary/60"
          >
        </div>

        <!-- Input Valor -->
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-primary">
            <DollarSign class="w-5 h-5" />
          </div>
          <input 
            v-model="form.valor" 
            type="text" 
            inputmode="decimal"
            placeholder="Valor da Venda"
            required
            class="w-full pl-12 pr-4 py-3 bg-white/50 border border-primary/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-primary focus:bg-white transition-all text-text-primary placeholder:text-text-secondary/60"
          >
        </div>

        <!-- Input Quantidade -->
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-primary">
            <Package class="w-5 h-5" />
          </div>
          <input 
            v-model="form.quantidade" 
            type="number" 
            min="1"
            placeholder="Quantidade"
            required
            class="w-full pl-12 pr-4 py-3 bg-white/50 border border-primary/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-primary focus:bg-white transition-all text-text-primary placeholder:text-text-secondary/60"
          >
        </div>

        <!-- Input Observações -->
        <div class="relative">
          <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-primary">
            <MessageSquare class="w-5 h-5" />
          </div>
          <input 
            v-model="form.observacoes" 
            type="text" 
            placeholder="Observações (Opcional)"
            class="w-full pl-12 pr-4 py-3 bg-white/50 border border-primary/20 rounded-2xl focus:outline-none focus:ring-2 focus:ring-primary focus:bg-white transition-all text-text-primary placeholder:text-text-secondary/60"
          >
        </div>

        <!-- Messages -->
        <p v-if="errorMessage" class="text-error text-center text-sm font-medium animate-pulse">{{ errorMessage }}</p>
        
        <!-- Submit Button -->
        <button 
          type="submit"
          :disabled="isLoading"
          class="w-full mt-2 flex items-center justify-center gap-2 bg-primary hover:bg-primary/90 disabled:opacity-70 disabled:cursor-not-allowed text-white font-medium py-4 px-6 rounded-full shadow-lg hover:shadow-xl transition-all duration-300"
        >
          <Heart class="w-5 h-5" :class="{ 'animate-ping': isLoading }" />
          <span>{{ isLoading ? 'REGISTRANDO...' : 'REGISTRAR COM AMOR' }}</span>
        </button>
      </form>
    </div>

    <!-- Floating Success Toast -->
    <transition name="slide-fade">
      <div v-if="successMessage" class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-success text-white px-6 py-3 rounded-full shadow-2xl font-medium tracking-wide flex items-center gap-2 z-50 whitespace-nowrap">
        <CheckCircle class="w-5 h-5" />
        {{ successMessage }}
      </div>
    </transition>
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

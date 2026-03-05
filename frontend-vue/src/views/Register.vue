<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ArrowLeft, Gift, DollarSign, Hash, MessageSquare, Heart, CheckCircle } from 'lucide-vue-next'
import { createSale } from '../services/api'

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
        <h2 class="text-xl font-body font-semibold text-primary">Destaque do Dia</h2>
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
            <Hash class="w-5 h-5" />
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

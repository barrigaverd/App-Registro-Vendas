<script setup>
import { useRouter } from 'vue-router'
import { CheckCircle, History } from 'lucide-vue-next'

const router = useRouter()

const goRegister = () => router.push('/register')
const goHistory = () => router.push('/history')
</script>

<template>
  <div class="w-full">
    <!-- Main Card -->
    <div class="glass-card flex flex-col items-center justify-center p-10 h-[400px] text-center">
      
      <!-- Titles -->
      <div class="space-y-2 mb-10">
        <h2 class="font-heading text-4xl font-bold text-text-primary">
          Vendeu
        </h2>
        <h1 class="font-accent text-6xl text-primary drop-shadow-sm">
          Amor?
        </h1>
      </div>

      <!-- Action Buttons -->
      <div class="w-full max-w-[250px] space-y-4">
        <button 
          @click="goRegister"
          class="w-full flex items-center justify-center gap-2 bg-primary hover:bg-primary/90 text-white font-medium py-4 px-6 rounded-full shadow-lg hover:shadow-xl transition-all duration-300 transform hover:-translate-y-1 active:translate-y-0"
        >
          <CheckCircle class="w-5 h-5" />
          SIM, Vendi!
        </button>

        <button 
          @click="goHistory"
          class="w-full flex items-center justify-center gap-2 bg-transparent hover:bg-black/5 text-text-secondary font-medium py-3 px-6 rounded-full transition-colors duration-300"
        >
          <History class="w-5 h-5" />
          Ver Histórico
        </button>
      </div>

    </div>
  </div>
</template>

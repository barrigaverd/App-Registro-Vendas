<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  title: String,
  value: String,
  subtitle: String,
  icon: Object,
  iconColor: {
    type: String,
    default: 'text-primary'
  },
  iconBg: {
    type: String,
    default: 'bg-secondary/30'
  }
})
</script>

<template>
  <div class="bg-surface rounded-2xl p-6 shadow-sm border border-gray-100 flex items-center gap-4 transition-transform hover:scale-[1.02]">
    <div :class="['p-4 rounded-xl shrink-0', iconBg]">
      <component :is="icon" :class="['w-6 h-6', iconColor]"></component>
    </div>
    
    <div>
      <h3 class="text-sm font-medium text-text-secondary">{{ title }}</h3>
      <p class="text-2xl font-bold text-text-primary mt-1">{{ value }}</p>
      <p v-if="subtitle" class="text-xs text-text-secondary mt-1">{{ subtitle }}</p>
    </div>
  </div>
</template>

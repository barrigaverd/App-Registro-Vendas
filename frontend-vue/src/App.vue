<script setup>
import { RouterView } from 'vue-router'
</script>

<template>
  <main class="min-h-screen bg-background text-text-primary font-body flex items-center justify-center p-4">
    <!-- Router view with transitions -->
    <router-view v-slot="{ Component }">
      <transition name="slide-fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </main>
</template>

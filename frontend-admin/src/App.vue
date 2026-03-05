<script setup>
import { RouterView } from 'vue-router'
import { LayoutDashboard, LogOut } from 'lucide-vue-next'
</script>

<template>
  <div class="min-h-screen bg-background flex flex-col md:flex-row">
    <!-- Sidebar -->
    <aside class="w-full md:w-64 bg-surface border-r border-gray-200 flex flex-col">
      <div class="h-16 flex items-center justify-center border-b border-gray-200">
        <h1 class="text-2xl font-heading text-primary font-bold">Vendeu Amor <span class="text-sm font-body text-text-secondary font-normal ml-1">Admin</span></h1>
      </div>
      <nav class="flex-1 p-4 space-y-2">
        <a href="/" class="flex items-center gap-3 px-4 py-3 bg-secondary/20 text-text-primary rounded-lg transition-colors hover:bg-secondary/40 font-medium">
          <LayoutDashboard class="w-5 h-5 text-primary" />
          Dashboard
        </a>
      </nav>
      <div class="p-4 border-t border-gray-200">
        <button class="w-full flex items-center justify-center gap-2 px-4 py-2 text-text-secondary hover:text-error transition-colors rounded-lg">
          <LogOut class="w-4 h-4" />
          Sair
        </button>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 overflow-auto">
      <RouterView />
    </main>
  </div>
</template>

<style>
/* Ocultei a scrollbar global para uma UI mais limpa */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: #E5989B;
  border-radius: 10px;
}
</style>

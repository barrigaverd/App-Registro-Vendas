# Plano do Projeto: Dashboard Admin Web

## Visão Geral
Criação de um Web App leve e responsivo (Dashboard Admin) para visualização, filtro e gestão manual (visual) das vendas registradas no banco de dados da API hospedada no VPS. O objetivo é facilitar a conferência para lançamentos manuais em outro software financeiro.

---

## 🏗️ Tipo de Projeto
**WEB** (Vue.js + TailwindCSS)
> *Agentes recomendados: `frontend-specialist`, `clean-code`*

---

## 🎯 Critérios de Sucesso
- Acessar os dados da API remota (`http://191.252.179.51:8001/vendas/`).
- Exibir os dados agrupados/filtráveis em 3 visões: **Dia, Semana e Mês (todos os meses)**.
- Implementar um mecanismo puramente visual (e efêmero na sessão) de "checkbox de lançado".
- Interface premium mantendo os tokens de design do app "Vendeu Amor" (cores, tipografia, cantos arredondados).
- Dashboard com resumo estatístico (Cards: Total Arrecadado, Qtd. Vendas, Ticket Médio).

---

## 🛠️ Stack Tecnológico
- **Framework:** Vue.js 3 (Composition API, `<script setup>`)
- **Build Tool:** Vite
- **Estilização:** TailwindCSS v3 (reutilizando cores personalizadas)
- **Requisições API:** Axios
- **Ícones:** Lucide-vue-next
- **Roteamento:** Vue Router

---

## 📁 Estrutura de Arquivos Prevista

```text
/frontend-admin/
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
├── src/
│   ├── main.js
│   ├── App.vue
│   ├── assets/
│   │   └── tailwind.css
│   ├── components/
│   │   ├── StatCard.vue       (Cards de resumo)
│   │   ├── SalesTable.vue     (Tabela principal com checkbox)
│   │   ├── FilterGroup.vue    (Botões de navegação tempo)
│   │   └── Header.vue
│   ├── views/
│   │   └── DashboardView.vue
│   └── services/
│       └── api.js             (Chamadas Axios para o VPS)
```

---

## 🚥 Divisão de Tarefas

| ID | Tarefa | Agente Recomendado | Input → Output → Verify |
|---|---|---|---|
| **T1** | Criar base do projeto Web Vue | `frontend-specialist` | Instalar framework e Tailwind → App.vue com layout base → Dev server abre `localhost` |
| **T2** | Configurar service de API (Axios) | `app-builder` | Configurar Axios para IP do VPS → Função getVendas → Teste no console se retorna os dados |
| **T3** | Criar Layout Base & Componentes | `frontend-specialist` | Gerar StatCard, FilterGroup e NavBar → Componentes em tela → Layout deve parecer responsivo e premium |
| **T4** | Lógica de Filtros (Dia/Sem/Mês) | `frontend-specialist` | Input de vendas da API → Lista filtrada reativamente baseado na aba escolhida → Tabela muda rápido |
| **T5** | Construir Tabela com Checkbox | `frontend-specialist` | Lista filtrada → Tabela com coluna "Lançado" (estado visual local) → Clicar marca/desmarca a cor da linha |
| **T6** | Cards Estatísticos Dinâmicos | `frontend-specialist` | Lista filtrada → Total/Tickets/Contagem calculados → Cards exibem valores formatados em R$ |

---

## ✅ PHASE X: Verificação Final
Para considerar o Dashboard concluído:

- [ ] Dev Server sobe corretamente e consome Mocks/API (CORS resolvido)
- [ ] Nenhum erro vermelho de Vue/Hydration no Console
- [ ] Checkbox "Lançado" funciona mas não quebra se fizer refresh
- [ ] Cálculos de Semana/Mês batem com a lógica temporal
- [ ] Interface não tem cores proibidas (`purple/violet`)

---
**Status do Plano:** Aprovado. Pronto para `/create` ou iniciar manualmente T1.

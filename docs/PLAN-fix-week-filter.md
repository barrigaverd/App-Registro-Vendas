# Plan: fix-week-filter

## 1. Overview
The user reports that the "semana" filter doesn't show expected results after a pull. This is likely because the filter currently uses the "current calendar week" (starting Sunday), which can be empty if today is early in the week or if recent sales fall just before Sunday. We will change this to "last 7 days" for a more intuitive experience.

## 2. Proposed Changes

### Frontend: DashboardView.vue
- **Update** `vendasFiltradas` computed property:
  - `hoje`: Same calendar day (local).
  - `semana`: Last 7 days (`now - 7*24h`).
  - `mes`: Last 30 days (`now - 30*24h`).
  - Add `console.log` in `carregarVendas` to show count of items.

### Frontend: api.js
- **Refinement:** Use regex `!/[+-]\d{2}:\d{2}$|Z$/.test(v.data)` to safely append `Z` only if no timezone indicator is present.

## 3. Verification Plan

### Manual Verification
1. Click "Hoje" -> Confirm sales from today appear.
2. Click "Semana" -> Confirm sales from the last 7 days appear.
3. Click "Mes" -> Confirm sales from the last 30 days appear.
4. Check browser console for data count.

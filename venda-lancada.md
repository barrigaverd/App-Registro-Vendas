# Plano de Implementação: Venda Lançada

## Overview
O objetivo deste plano é finalizar a implementação da coluna `venda_lancada` no back-end e integrar o funcionamento do marcador correspondente no painel de administração (Frontend Vue). Com esta alteração, os dados de "Lançado" não serão mais efêmeros no navegador, mas sim persistidos no banco de dados.

## Project Type
**WEB / BACKEND**

## Success Criteria
- A coluna `venda_lancada` deve ser persistida corretamente no banco de dados.
- O back-end deve aceitar atualizações no status de `venda_lancada` através de chamadas à API `PUT /vendas/{id}`.
- O painel de administração (`frontend-admin`) deve refletir o estado de `venda_lancada` vindo do back-end.
- Ao clicar no checkbox "Lançado" no admin, a ação deve atualizar o banco de dados de forma assíncrona.

## Tech Stack
- **Back-end:** FastAPI, SQLAlchemy, Pydantic, SQLite (ou Postgres dependendo do seu setup local).
- **Front-end / Admin:** Vue.js, Axios, Tailwind CSS.

## File Structure Atingida
```
backend/
├── models.py
├── crud.py
frontend-admin/
├── src/
│   ├── services/
│   │   └── api.js
│   └── views/
│       └── DashboardView.vue
```

## Task Breakdown

### Tarefa 1: Corrigir o Modelo do Banco de Dados (`backend/models.py`)
**Agent**: `backend-specialist` | **Skills**: `clean-code`
- **Por que**: A coluna `venda_lancada` já foi declarada na classe `Venda`, porém o tipo `Boolean` não foi importado, o que causará erro na inicialização do SQLAlchemy.
- **INPUT**: `backend/models.py`
- **OUTPUT**:
  - Na linha 2, adicione `Boolean` na importação: `from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean`.
- **VERIFY**: Rode a aplicação (`uvicorn database:app --reload` ou similar dependendo de `main.py`) e verifique se não há erros de importação ("NameError: name 'Boolean' is not defined").
- **Nota**: Se você estiver utilizando o SQLite com Alembic, emita a migração para adicionar a coluna na tabela existente, ou caso seja ambiente de teste, recrie o banco. 

### Tarefa 2: Atualizar o CRUD para Salvar a Alteração (`backend/crud.py`)
**Agent**: `backend-specialist` | **Skills**: `clean-code`
- **Por que**: A função `update_venda` não está transferindo o novo valor de `venda_lancada` recebido pelo schema para o banco de dados.
- **INPUT**: `backend/crud.py`
- **OUTPUT**:
  - Dentro da função `update_venda`, após atualizar as observações (linha 35), adicione a instrução para salvar o booleano:
  ```python
  if venda_update.venda_lancada is not None:
      db_venda.venda_lancada = venda_update.venda_lancada
  ```
- **VERIFY**: Faça uma chamada manual para `PUT /vendas/{id}` com um JSON contendo `"venda_lancada": true` e verifique se retorna atualizado.

### Tarefa 3: Adicionar a Chamada de Atualização na API do Frontend (`frontend-admin/src/services/api.js`)
**Agent**: `frontend-specialist` | **Skills**: `clean-code`
- **Por que**: O Front-end precisa enviar o comando HTTP PUT para o servidor.
- **INPUT**: `frontend-admin/src/services/api.js`
- **OUTPUT**:
  - Adicione a função exportada para atualizar a venda:
  ```javascript
  export const updateVenda = async (id, vendaData) => {
    const response = await api.put(`/vendas/${id}`, vendaData);
    return response.data;
  };
  ```
- **VERIFY**: Verifique se a função foi devidamente exportada.

### Tarefa 4: Integrar Estado Persistente no Dashboard (`frontend-admin/src/views/DashboardView.vue`)
**Agent**: `frontend-specialist` | **Skills**: `frontend-design`, `clean-code`
- **Por que**: O sistema atual usa um `Set()` efêmero chamado `lancados` para armazenar o estado das checkboxes, mas o estado deve ser inicializado pelo DB e salvo imediatamente nas alterações.
- **INPUT**: `frontend-admin/src/views/DashboardView.vue`
- **OUTPUT**:
  - Remova (ou altere) o `Set()` `lancados`.
  - Importe `updateVenda` de `../services/api.js`.
  - No bloco de `vendasFiltradas`, substitua os atalhos de `lancados.has(venda.id)` por `venda.venda_lancada`.
  - Refatore a função `toggleLancado(id)` (ou crie uma função similar `toggleLancado(venda)`) para enviar a atualização para o back-end via `updateVenda(venda.id, { ...venda, venda_lancada: !venda.venda_lancada })` e em seguida modifique o estado local do objeto na ref `vendas`.
- **VERIFY**: Abra a UI do painel admin interativo, marque o checkbox "Lançado". Recarregue a página (F5) para provar que a alteração foi mantida e não se perdeu.

## ✅ PHASE X COMPLETE
*Para ser preenchido por você (usuário) após a execução:*
- Lint: [ ] Pass
- Security: [ ] No critical issues
- Build: [ ] Success
- Date: [ ]

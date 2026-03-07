# Plano de Deploy na VPS: Frontend e Backend

## Visão Geral
Atualmente, o backend está rodando de forma improvisada na pasta `/root/backend` do VPS. O objetivo deste plano é padronizar o deploy via GitHub (Git Clone), servir o frontend Admin para ser acessível via internet (usando IP), configurar o novo backend a partir do repositório clonado e limpar a pasta temporária `/root`.

---

## 🏗️ Tipo de Projeto
**BACKEND / DEPLOYMENT** (Infraestrutura, Git, Nginx/Servidor Web)
> *Agentes recomendados: `devops-engineer` (se houvesse) ou `backend-specialist` / `orchestrator`*

---

## 🎯 Critérios de Sucesso
- Repositório local com **todas as alterações "commitadas" e "pushadas" (Push)** para a branch `main` no GitHub.
- Repositório **clonado** no VPS (ex: na pasta `/opt/App-Registro-Vendas` ou `/var/www/App-Registro-Vendas`).
- O **Backend FastAPI** rodando na nova pasta do clone (porta 8001 ou outra configurada).
- O **Frontend Admin** compilado (build) e sendo servido pela internet (utilizando Nginx, Caddy ou outro servidor simples no próprio VPS).
- Acesso comprovado ao Frontend Admin pelo IP do VPS (ex: `http://191.252.179.51`).
- O **APK (App do Usuário)** comunica perfeitamente com o novo backend (sem necessidade de rebuild caso a porta e o IP do backend permaneçam `8001` e `191.252.179.51`).
- A pasta provisória `/root/backend` deve ser **apagada**.

---

## 🛠️ Stack / Ferramentas
- **Controle de Versão:** Git (GitHub)
- **Servidor VPS:** Ubuntu/Linux
- **Servidor Web (Frontend):** Nginx (Recomendado) ou `http-server` do Node.js
- **Process Manager (Backend):** PM2 ou Systemd (para manter o FastAPI rodando em background)

---

## 🚥 Divisão de Tarefas

| ID | Tarefa | Agente Recomendado | Input → Output → Verify |
|---|---|---|---|
| **T1** | Commitar e fazer Push (PC Local) | `orchestrator` | `git add .`, `git commit`, `git push origin main` → Repositório no GitHub atualizado → Verificar status no GitHub remote. |
| **T2** | Preparar VPS e Clonar Repositório | `backend-specialist` | Acessar VPS, instalar `git` (se não tiver) e clonar em `/var/www/App-Registro-Vendas` → Pasta do projeto criada no VPS com os arquivos mais recentes → Verificar com `ls`. |
| **T3** | Configurar Novo Backend no VPS | `backend-specialist` | Criar venv, instalar `requirements.txt` da nova pasta e migrar banco SQLite se necessário (ou copiar o `vendas.db` antigo de `/root/backend` para não perder dados) → Iniciar o FastAPI pelo PM2/Systemd → Verificar `curl 127.0.0.1:8001`. |
| **T4** | Build P/ Produção do Front Admin | `frontend-specialist` | Configurar variáveis de ambiente no frontend para apontar para IP do VPS, rodar `npm install` e `npm run build` dentro da pasta clone no VPS (ou local e dar push) → Pasta `dist/` gerada. |
| **T5** | Servir o Frontend e Limpeza | `backend-specialist` | Configurar o Nginx apontando para a pasta `dist` do Frontend (ex: porta 80), e excluir (com segurança) a pasta `rm -rf /root/backend` → Acesso liberado no navegador da web e root limpo. |

---

## ✅ PHASE X: Verificação Final
Para considerar o deploy concluído:

- [ ] Arquivos do GitHub local e VPS estão sincronizados (mesmo hash no `git log`).
- [ ] Consegue-se acessar o Frontend Admin do PC ou celular usando apenas o IP do servidor (`http://191.252.179.51`).
- [ ] Consegue-se interagir com os dados normalmente pelo Painel Admim (Listar, Filtrar, Lançar).
- [ ] O App (APK) "Vendeu Amor" consegue gerar vendas sem erros com a nova API (se os dados entrarem no DB novo, está rodando 100%).
- [ ] A pasta `/root/backend` não existe mais no VPS.

---

> ⚠️ **Ponto de Atenção - Socratic Gate (Riscos / Decisões a serem tomadas):**
> 1. O banco de dados SQLite (`vendas.db`) que está preenchido com dados reais está dentro do `/root/backend`? Teremos que COPIAR esse arquivo para o clone novo em `/var/www` GANTES de deletar o diretório `/root/backend`, para você não perder todo seu histórico real. OK?
> 2. O seu repositório do GitHub é **privado**? Se for, precisaremos criar um Token (PAT) ou adicionar a chave SSH da VPS no seu GitHub para poder fazer o `git clone`.
> 3. Você quer servir o frontend Admin na porta 80 usando Nginx (o padrão mais seguro da internet), ou prefere outra solução mais simples?

---
**Status do Plano:** Gerado (Aguardando resposta do Socratic Gate / Revisão do Usuário).
Pronto para usar `/orchestrate` ou executar as tarefas (T1, T2...).

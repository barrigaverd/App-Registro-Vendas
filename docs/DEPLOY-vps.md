# Guia de Deploy do Backend (Debian VPS)

Este guia acompanha você desde a descoberta do IP da sua VPS até a publicação do seu backend FastAPI em produção.

## Passo 1: Descobrindo o IP da sua VPS

Como você se conecta à VPS dita como você descobre o IP:

**Caso A: Você ainda não acessou a VPS e precisa do IP para conectar via SSH.**
Neste caso, o IP público da sua máquina **sempre** fica no Painel de Controle da empresa onde você alugou o servidor (Ex: Hostinger, AWS, DigitalOcean, Linode, Google Cloud).
Lá vai ter algo como: `Endereço IP: 198.51.100.23`.

**Caso B: Você já está no terminal (tela preta) da VPS, mas não sabe o IP público dela.**
Digite este comando no terminal do Debian:
```bash
curl ifconfig.me
```
*Ele vai cuspir exatamente o IP que precisamos.*

---

## Passo 2: Preparando a VPS (Debian)

Entre na sua VPS via SSH:
```powershell
ssh root@SEU_IP_DA_VPS
```

Assim que entrar, atualize o servidor e instale o Python:
```bash
apt update && apt upgrade -y
apt install python3 python3-pip python3-venv -y
```

---

## Passo 3: Enviando os Arquivos para a VPS

No seu computador **Windows** (não na VPS), abra um novo terminal no PowerShell e envie a pasta do `backend` inteira (incluindo o `vendas.db` para não perder os dados) para a VPS usando SCP:

```powershell
scp -r "C:\Users\Sergio\Desktop\App-Registro-Vendas\backend" root@SEU_IP_DA_VPS:/root/backend
```

---

## Passo 4: Rodando a API na Nuvem

Volte para o terminal da **VPS**, entre na pasta e ligue a máquina:

```bash
cd /root/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### O Truque de Mestre (Screen)
Se você apenas rodar `uvicorn` e fechar a janela, o servidor cai. Vamos usar uma ferramenta chamada `screen` ou `tmux` para deixar rodando em segundo plano:

```bash
apt install screen -y
screen -S api_vendas
```
*(Você vai entrar numa "tela virtual")*

Agora rode o servidor abrindo para a internet inteira (`0.0.0.0`) e na porta `80`:
```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

Para **sair da tela sem desligar a API**, aperte:
`Ctrl + A`, solte, e depois aperte `D` (D de Detach).

---

## Passo 5: Atualizando o Celular

Agora que a API está rodando no IP: `http://SEU_IP_DA_VPS:80`, você precisará alterar aquela linha no código do Vue (`frontend-vue/src/services/api.js`) para apontar para o IP da VPS, gerar o APK de novo com `npm run build ; npx cap sync android ; $env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"; .\gradlew assembleDebug`, e instalar no celular da sua esposa.

Agora vai funcionar no 4G dela na rua, longe do Wi-Fi da sua casa!

# Guia de Build — APK Android (Vendeu Amor)

## Pré-requisitos

### 1. Flutter SDK
- Download: https://flutter.dev/docs/get-started/install/windows
- Adicionar ao PATH do sistema
- Verificar: `flutter doctor`

### 2. Android Studio
- Download: https://developer.android.com/studio
- Instalar: Android SDK, Android SDK Command-line Tools, NDK
- Aceitar licenças: `flutter doctor --android-licenses`

### 3. Verificar Setup Completo
```bash
flutter doctor
```
Todos os itens devem estar marcados com ✓

---

## Build do APK

```bash
cd "C:\Users\sergi\Desktop\App Registro Vendas\frontend"

# Instalar dependências
pip install -r requirements.txt

# Build APK
flet build apk --project "VendeuAmor"
```

APK gerado em: `frontend/build/apk/VendeuAmor.apk`

---

## Distribuição

### Instalar no Celular (Dev/Teste)
1. Habilitar **"Fontes desconhecidas"** no Android
2. Transferir o APK via USB, e-mail ou Google Drive
3. Abrir o arquivo no celular e instalar

### Play Store (Produção — Opcional)
- Gerar AAB: `flet build aab`
- Criar conta Google Play Developer (US$ 25 única vez)
- Submeter via Google Play Console

---

## Configurações do Backend em Produção

> [!IMPORTANT]
> O `api_service.py` aponta para `127.0.0.1:8001` (local).
> Para usar o app no celular, o backend deve estar acessível na rede.

**Opções:**
- **Mesma rede Wi-Fi:** Usar o IP local do PC (ex: `192.168.1.10:8001`) e rodar o uvicorn com `--host 0.0.0.0`
- **Nuvem:** Hospedar o FastAPI em serviço como Render, Railway, ou VPS

# Frontend Framework Migration Plan

## Overview
The user wants to replace BeeWare (Toga) with another framework that can perfectly replicate the beautiful "Stationery" visual aesthetic (rounded corners, soft shadows, custom fonts) that Flet provided, while ensuring the Android APK build actually works (which Flet failed at).

## Project Type
**MOBILE FRONTEND** connecting to an existing **PYTHON BACKEND (FastAPI)**.

## Framework Alternatives for "Beautiful Mobile UI"

### Opção 1: React Native com Expo (🏆 Recomendação Ouro)
- **O que é:** O padrão da indústria para apps mobile.
- **Visual:** 100% perfeito. Sombras delicadas, bordas, animações e fontes customizadas (idêntico ao design original).
- **Linguagem:** TypeScript/JavaScript (apenas no frontend, o backend continua em Python/FastAPI).
- **Build APK:** Muito mais fácil. Pode ser feito localmente ou na nuvem da Expo sem dor de cabeça no Windows.
- **Agente Responsável:** `mobile-developer`

### Opção 2: KivyMD (Python)
- **O que é:** Framework Python com interface focada em Material Design (semelhante ao Flet).
- **Visual:** Chega muito perto do Flet, focado em mobile.
- **Linguagem:** 100% Python.
- **Build APK:** Usa o *Buildozer*. **Problema:** O Buildozer só roda em Linux. Como você está no Windows, precisaria usar o WSL (Windows Subsystem for Linux) ou uma máquina virtual para gerar o APK.
- **Agente Responsável:** `frontend-specialist` / `mobile-developer`

## Socratic Gate (User Decision Required)
We must pause the planning here and ask the user which path to take:
1. **React Native (Expo):** Visual impecável e build de APK fácil na nuvem, mas troca a linguagem do frontend para JavaScript.
2. **KivyMD:** Mantém tudo em Python e tem visual bonito, mas o processo de gerar o APK no Windows é mais trabalhoso (exige WSL/Linux).

## Next Steps once Decided
If **React Native**:
- Scaffold Expo project.
- Recreate `HomeView`, `RegistrationView`, and `HistoryView` in React Native.
- Connect using `fetch` or `axios` to FastAPI.

If **KivyMD**:
- Setup KivyMD environment.
- Rewrite views using KivyMD components.
- Setup WSL for Buildozer.

## Verification
- [ ] User selects the framework.
- [ ] Task breakdown is updated based on selection.
- [ ] UI is implemented.
- [ ] APK is successfully built and tested.

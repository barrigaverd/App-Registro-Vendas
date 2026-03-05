---
description: Build do APK Android para o projeto Vue + Capacitor (Vendeu Amor)
---

# ⚠️ Pré-requisitos Obrigatórios

## Versões Comprovadas (funcionam em 05/03/2026)

| Componente        | Versão Correta              | Onde fica                                              |
|-------------------|-----------------------------|--------------------------------------------------------|
| **JAVA_HOME**     | OpenJDK 21 (Android Studio) | `C:\Program Files\Android\Android Studio\jbr`         |
| **Gradle**        | 8.13                        | `frontend-vue\android\gradle\wrapper\gradle-wrapper.properties` |
| **AGP**           | 8.13.0                      | `frontend-vue\android\build.gradle` linha `classpath` |

> ⚠️ O Java padrão do sistema é Java 25 — **NÃO usar**. Ele é incompatível com o AGP e o Gradle.
> Sempre forçar JAVA_HOME para o JDK do Android Studio antes de buildar.

---

# Passos do Build

## 1. Build do Vue (gera a pasta `dist`)

Rodar a partir de: `frontend-vue\`

```powershell
npm run build
```

## 2. Sincronizar com Android (Capacitor)

Rodar a partir de: `frontend-vue\`

```powershell
npx cap sync android
```

## 3. Gerar o APK via Gradle

Rodar a partir de: `frontend-vue\android\`

```powershell
$env:JAVA_HOME = "C:\Program Files\Android\Android Studio\jbr"
.\gradlew assembleDebug
```

## APK gerado em:

```
frontend-vue\android\app\build\outputs\apk\debug\app-debug.apk
```

---

# Diagnóstico de Erros Comuns

| Erro                                  | Causa                                  | Solução                                                                 |
|---------------------------------------|----------------------------------------|-------------------------------------------------------------------------|
| `Unsupported class file major version 69` | Java 25 incompatível com Gradle/AGP | Definir `$env:JAVA_HOME` para o JDK 21 do Android Studio               |
| `Minimum supported Gradle version is X` | Gradle desatualizado para o AGP usado | Atualizar `distributionUrl` no `gradle-wrapper.properties`              |
| `android platform has not been added` | Comando rodado da pasta errada         | Rodar `npx cap sync android` a partir de `frontend-vue\`, não `android\`|
| `BUILD FAILED in ~800ms`              | Java errado sem logs claros            | Sempre definir JAVA_HOME antes do gradlew                               |

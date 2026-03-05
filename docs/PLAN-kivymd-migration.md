# KivyMD Framework Migration Plan

## Overview
The user selected Option 2: migrating the frontend from BeeWare (Toga) to **KivyMD (Python)**. KivyMD will allow us to stay 100% in Python while taking advantage of Material Design components that closely match the original Flet look (cards, shadows, rounded corners, icons). The backend will remain the existing FastAPI service. 

## Project Type
**MOBILE FRONTEND** connecting to an existing **PYTHON BACKEND (FastAPI)**. Primary Agent: `mobile-developer` & `frontend-specialist`.

## Success Criteria
- The app must use KivyMD components (MDCard, MDLabel, MDTextField, etc.) to recreate the beautiful "Stationery" visual aesthetic.
- The UI must have proper spacing, rounded corners, shadows, and custom colors matching the original Flet theme (Rosa/Roxo suaves).
- The app must connect asynchronously to the FastAPI backend (`http://127.0.0.1:8001`) using `httpx` or `aiohttp` or Kivy's `UrlRequest`.
- The final code structure must be ready for Buildozer to generate the APK (even though Buildozer requires Linux/WSL, we must prepare the `buildozer.spec` file).

## Tech Stack
- Frontend: `kivy`, `kivymd` (Python)
- HTTP Client: Kivy's `UrlRequest` (or `kivy.network.urlrequest`) or `httpx` with `grequests`/`asyncio` adapters, as Kivy runs its own event loop.
- Packaging: `buildozer` (requires WSL/Linux for Android APK).

## File Structure
```
c:/Users/Sergio/Desktop/App-Registro-Vendas/
├── main.py                (KivyMD entry point)
├── buildozer.spec         (Buildozer configuration for APK)
├── requirements.txt       (KivyMD dependencies)
├── views/
│   ├── __init__.py
│   ├── home_view.py       (Dashboard UI)
│   ├── registration_view.py (Form UI)
│   └── history_view.py    (Sales list UI)
├── services/
│   ├── __init__.py
│   └── api_service.py     (API interaction)
└── theme.py               (Color and styling constants)
```

## Task Breakdown

### Task 1: Environment Setup
- **Agent:** `orchestrator`
- **INPUT:** Clean up previous Toga/Briefcase files if needed, or just set up the new structure.
- **OUTPUT:** `requirements.txt` with `kivy`, `kivymd`, etc.
- **VERIFY:** Dependencies listed correctly.

### Task 2: Core Architecture & Theme
- **Agent:** `frontend-specialist`
- **INPUT:** The "Stationery" theme colors.
- **OUTPUT:** `theme.py` and `main.py` configuring the `MDApp` and ScreenManager.
- **VERIFY:** The app launches successfully on the desktop.

### Task 3: Views Implementation
- **Agent:** `mobile-developer`
- **INPUT:** `HomeView`, `RegistrationView`, `HistoryView`.
- **OUTPUT:** Functional KivyMD screens with `MDCards`, icons, and inputs.
- **VERIFY:** UI looks significantly better ("lindo do jeito que estava").

### Task 4: API Integration
- **Agent:** `backend-specialist`
- **INPUT:** KivyMD views and FastAPI endpoints.
- **OUTPUT:** `api_service.py` using Kivy-compatible async requests handling the event loop properly.
- **VERIFY:** Data can be sent to and fetched from the FastAPI backend.

### Task 5: Buildozer Spec Setup
- **Agent:** `devops-engineer`
- **INPUT:** The working KivyMD app.
- **OUTPUT:** `buildozer.spec` file configured for Android.
- **VERIFY:** The spec file contains all necessary requirements and permissions (INTERNET).

## Phase X: Verification
- [ ] UI looks polished and resembles the original Flet app.
- [ ] Navigation between screens works natively in KivyMD.
- [ ] API requests succeed without blocking the UI thread.

## ✅ PHASE X COMPLETE
- Lint: [ ]
- Build: [ ]
- Date: Pending

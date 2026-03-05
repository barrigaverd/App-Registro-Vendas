# Frontend Migration Plan: Vue 3 + TailwindCSS + Capacitor

## 🔴 Overview
The user selected **Option 1**: migrate the frontend to a Web Framework to guarantee beautiful formatting (rounded cards, native shadows, SVG icons, smooth transitions) leveraging TailwindCSS, connecting to the FastAPI backend, and wrapping the final product in Capacitor for an Android APK. 
Given its intuitive syntax and excellent transition handling, we will utilize **Vue 3 (Composition API)** to build out the "Vendeu Amor" front-end.

## 📱 Project Type
**WEB** (Progressive Web Application / Hybrid Mobile App via Capacitor)

## 🏗️ Technical Stack
- **Framework:** Vue 3 (Composition API, `<script setup>`)
- **Bundler:** Vite
- **Styling:** TailwindCSS v3 (for utility-class ease)
- **Icons:** Lucide-Vue-Next (SVG icons as per UI/UX Pro Max rules)
- **Routing:** Vue Router (for home/register/history transitions)
- **State/HTTP:** Axios or native Fetch directly to `http://127.0.0.1:8001`
- **Mobile Packaging:** Capacitor.js (Future step for Android APK)

## 🎨 UI/UX Pro Max Architecture (Stationery Theme)
We will enforce the exact aesthetic guidelines generated from the `ui-ux-pro-max` Search:
1. **No Emoji Icons:** We will strictly use SVGs (Lucide) for UI interactions.
2. **Stable Hover States:** Use `transition-all duration-300` for color and soft-shadow changes without shifting the element.
3. **Typography:** Use the downloaded or CDN versions of:
   - Heading: `Great Vibes` (for "Amor") / `Cormorant Infant`
   - Body/Inputs: `Outfit`
4. **Light Mode High Contrast:** Text will map to `#374151` and borders/shadows will remain soft but visible.
5. **Glass/Soft Cards:** Apply Tailwind `bg-white shadow-xl rounded-3xl` classes for depth.

## 🗂️ File Structure
```
c:\Users\Sergio\Desktop\App-Registro-Vendas\
├── backend/                  # (Untouched FastAPI Code)
├── frontend-vue/             # [NEW] Entire web frontend app lives here
│   ├── index.html            # Main entry
│   ├── package.json          # Dependencies (vue, tailwind, etc)
│   ├── src/
│   │   ├── main.js           # Vue init
│   │   ├── style.css         # Tailwind Core + Font Imports + Root Vars
│   │   ├── App.vue           # Router View + Global Transitions
│   │   ├── router.js         # Navigation configs
│   │   ├── services/
│   │   │   └── api.js        # Axios connection to localhost:8001
│   │   ├── views/
│   │   │   ├── Home.vue      # Dashboard ("SIM Vendi", "Histórico")
│   │   │   ├── Register.vue  # Input Form
│   │   │   └── History.vue   # Sales Cards
│   └── ...
```

## 📋 Task Breakdown

### 1. Project Initialization & Setup
- `[ ]` Scaffold Vue 3 app (`npx create-vue@latest frontend-vue` equivalent setup).
- `[ ]` Install TailwindCSS, Vue Router, and Lucide Icons.

### 2. Theming & Global Styling
- `[ ]` Configure `tailwind.config.js` with the Stationery Color Palette (`#E5989B`, `#FFCDD2`, etc) and Fonts.
- `[ ]` Embed the Google Fonts (Great Vibes, Cormorant, Outfit) into `index.html`.
- `[ ]` Setup global CSS transitions (`style.css`).

### 3. Core Vue Logic
- `[ ]` Setup Vue Router (`src/router.js`).
- `[ ]` Setup API Service (`src/services/api.js`) to connect to the backend.

### 4. Component Construction (Views)
- `[ ]` `Home.vue`: Implement the centered floating glass card, "Vendeu Amor?" titles, and large primary action buttons.
- `[ ]` `Register.vue`: Implement Tailwind Floating Labels or clean inset inputs with SVG icons. Hook up API POST.
- `[ ]` `History.vue`: Implement vertical scrolling list of Tailwnd cards displaying the sales. Hook up API GET/DELETE.

## ✅ Phase X: Verification Matrix
- [ ] Backend is running (`uvicorn`).
- [ ] Web frontend starts on `localhost` (vite).
- [ ] UI looks perfectly smooth (shadows, fonts, SVGs).
- [ ] Transitions between routes feel like a native mobile app.
- [ ] Form submits successfully to FastAPI database.

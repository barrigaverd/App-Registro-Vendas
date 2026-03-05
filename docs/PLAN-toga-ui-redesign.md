# Toga UI Redesign Plan

## Overview
The goal is to redesign the newly migrated Toga API frontend for the "Vendeu Amor" app. The user noted that the transition from Flet to Toga lost the "beautiful," highly-styled "Stationery" aesthetic (rounded corners, shadows, icons, specific fonts). We will plan to restore as much of that aesthetic as possible within BeeWare/Toga's limitations, or by using WebViews.

## Project Type
**MOBILE / DESKTOP (BeeWare / Python)** - Primary Agent: `mobile-developer` / `frontend-specialist` (if WebView).

## Success Criteria
- The app must visually resemble the original Flet layout and color theme.
- The UI must have properly padded, responsive containers.
- Typography must be distinctive (either custom loaded fonts or well-selected native alternatives).
- Inputs, labels, and buttons must not feel bare-bones or "ugly."

## Tech Stack
- Python 3.9+
- BeeWare / Toga framework
- (Optional) `toga.WebView` + HTML/CSS if exact 1:1 pixel styling is demanded.

## Socratic Gate Context (Pending User Output)
The capabilities of Toga natively are limited regarding Box Shadows, complex border radii across all platforms, and built-in icon libraries. We must clarify with the user if they want to build complex HTML/CSS WebViews for the exact look or push the boundaries of Toga's native `Pack` stylings.

## File Structure
```
src/vendeu_amor/
├── app.py
├── components/          (If modularized further)
│   ├── buttons.py
│   └── cards.py
├── resources/
│   ├── fonts/           (For .ttf files)
│   └── icons/           (For .png vectors)
```

## Task Breakdown

### Task 1: UI Strategy Decision (Agent: `orchestrator`)
- **INPUT:** Understand user preference (Native Toga vs WebView).
- **OUTPUT:** Chosen rendering path.
- **VERIFY:** User explicitly confirms the path.

### Task 2: Resource Gathering (Agent: `mobile-developer`)
- **INPUT:** Decision from Task 1. Needs fonts and icons.
- **OUTPUT:** `resources/` folder populated with required `.ttf` and `.png`/`.jpeg` assets.
- **VERIFY:** Files exist in the system and are accessible by Briefcase.

### Task 3: Layout Refactoring (Agent: `mobile-developer`)
- **INPUT:** Existing `app.py` logic.
- **OUTPUT:** New component structures using `Pack(flex=1, padding=X, background_color=Y)` properly nested to simulate "Cards", OR a built `index.html` file loaded into a `toga.WebView`.
- **VERIFY:** App renders visually pleasing layouts in `briefcase dev`.

### Task 4: Custom Font Integration (if Native) (Agent: `mobile-developer`)
- **INPUT:** Font files.
- **OUTPUT:** Code using `toga.Font.register("FontName", "resources/fonts/Font.ttf")` and applying them to Labels/Buttons.
- **VERIFY:** Fonts render correctly on screen.

## Phase X: Verification
- [ ] UI looks polished, not bare-bone.
- [ ] No `briefcase dev` compilation errors.
- [ ] Navigation components are properly styled.
- [ ] `briefcase build android` finishes successfully without packaging errors.

## ✅ PHASE X COMPLETE
- Lint: [ ]
- Build: [ ]
- Date: Pending

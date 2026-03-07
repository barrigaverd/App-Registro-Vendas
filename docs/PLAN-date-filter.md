# PLAN: date-filter

## 1. Overview
The goal is to properly implement the "today, week, month" front-end filters in the Dashboard and resolve existing backend merge conflicts. The Vue dashboard currently downloads all sales and filters them locally based on `v.data`, but naive string parsing causes a timezone offset bug. Also, recent git pulls resulted in merge conflicts in the backend models and CRUD operations for the `lancado` feature.

## 2. Project Type
**WEB + BACKEND**

## 3. Success Criteria
1. The Vue dashboard accurately filters "hoje", "semana", and "mes" using correct local time handling.
2. The backend code runs without syntax errors or merge conflict markers (`<<<<<<< HEAD`).
3. The `lancado` status correctly toggles on the dashboard and persists in the backend.

## 4. Tech Stack
- Frontend: Vue 3, Vite, TailwindCSS
- Backend: Python, FastAPI, SQLAlchemy

## 5. File Structure
### Affected Files
- `backend/models.py`
- `backend/crud.py`
- `frontend-admin/src/views/DashboardView.vue`

## 6. Task Breakdown

### Task 1: Resolve Git Merge Conflicts
- **Agent:** `backend-specialist`
- **Description:** Remove the git merge markers in `backend/models.py` and `backend/crud.py`. Consolidate the `venda_lancada` and `lancado` fields, keeping `lancado` because the frontend already expects and uses `lancado`.
- **INPUT → OUTPUT → VERIFY:**
  - Input: `backend/models.py`, `backend/crud.py`
  - Output: Conflict-free Python files using `lancado = Column(Boolean, default=False)`.
  - Verify: Run `python -m mypy` or start the FastAPI server to ensure it runs without syntax errors.

### Task 2: Fix Date Timezone Parsing
- **Agent:** `frontend-specialist`
- **Description:** Adjust the date parsing in `DashboardView.vue`. The backend stores dates in UTC and returns them as naive strings (e.g., `2026-03-07T14:41:42`). The frontend `new Date(v.data)` parses this as local time, shifting it by the user's timezone offset and breaking the "today" filter around midnight.
- **INPUT → OUTPUT → VERIFY:**
  - Input: `frontend-admin/src/views/DashboardView.vue`
  - Output: Append `'Z'` to `v.data` before passing it to `new Date()` (i.e. `new Date(v.data + 'Z')`), converting UTC to local time accurately. 
  - Verify: Filter the dashboard for 'hoje' and confirm sales created today show up correctly.

### Task 3 (Optional for Scaling): Move Filtering to Backend
- **Agent:** `backend-specialist` / `frontend-specialist`
- **Description:** For better scalability instead of loading all `vendas`, add `data_inicio` and `data_fim` query params in `crud.py` and update the Vue dashboard to fetch only the required timeframe.
- **INPUT → OUTPUT → VERIFY:**
  - Input: Backend routes / Vue API service
  - Output: Server-side API date filtering.
  - Verify: Network tab shows smaller JSON payloads in requests.

## ✅ Phase X: Verification
- [ ] Backend runs successfully and API responds to `/vendas/`
- [ ] No `<<<<<<< HEAD` markers remaining in any file
- [ ] Frontend dashboard correctly filters the current day, week, and month without timezone drift
- [ ] Socratic Gate was respected during planning

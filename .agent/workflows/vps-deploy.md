---
description: Push local changes, pull on VPS, and restart the backend.
---

# /vps-deploy - Automated VPS Deployment

// turbo-all

## Logic

1. **Local Push**
   ```powershell
   git add . ; git commit -m "deploy: automated update" ; git push origin main
   ```

2. **VPS Pull & Restart**
   Connect to `root@191.252.179.51` and execute:
   ```bash
   cd /var/www/App-Registro-Vendas
   git reset --hard HEAD
   git pull origin main
   
   # Restart Backend
   pkill uvicorn
   cd backend
   source venv/bin/activate
   nohup uvicorn main:app --host 0.0.0.0 --port 8001 > backend.log 2>&1 &
   
   # Restart Frontend (Nginx is usually enough, but if dist changed via push)
   # systemctl reload nginx
   ```

3. **Verification**
   ```bash
   curl -sI http://127.0.0.1:8001 | head -n 1
   ```

---

## Usage

Run `/vps-deploy` to synchronize local changes with the production server.

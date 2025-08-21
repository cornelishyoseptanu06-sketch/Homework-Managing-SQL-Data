# FastAPI Codespaces Starter

A minimal, ready-to-run FastAPI project configured for **GitHub Codespaces**.

## How to use (GitHub Codespaces)
1. **Upload to GitHub**:
   - Create a new repository on GitHub (public or private).
   - Upload all files from this folder (including the `.devcontainer` directory).

2. **Open in Codespaces**:
   - On your repo page, click **Code** → **Create codespace on main**.
   - Wait for the container to finish setup (it will auto-install Python deps).

3. **Run the app**:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
   Codespaces will auto-forward port **8000** and open the browser.

## Run locally (optional)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Open http://localhost:8000 and http://localhost:8000/docs

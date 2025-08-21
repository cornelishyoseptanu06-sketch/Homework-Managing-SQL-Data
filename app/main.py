from fastapi import FastAPI

app = FastAPI(title="Hello Codespaces")

@app.get("/")
def read_root():
    return {"message": "Hello from Codespaces! 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

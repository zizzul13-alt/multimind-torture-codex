"""Benchmark seam: a real FastAPI contract, not a production orchestration copy."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="MultiMind Benchmark Seam", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://127.0.0.1:4173"], allow_methods=["GET"], allow_headers=["*"])

class Agent(BaseModel):
    name: str
    state: str
    progress: int

@app.get("/health")
def health():
    return {"status": "ok", "service": "fastapi-benchmark-seam"}

@app.get("/api/session")
def session():
    return {
        "id": "mm-2048", "user": "Mira Chen", "topic": "Port city climate adaptation",
        "agents": [
            Agent(name="Research", state="RUNNING", progress=72),
            Agent(name="Critic", state="WAITING", progress=43),
            Agent(name="Synthesis", state="PENDING", progress=12),
        ],
    }

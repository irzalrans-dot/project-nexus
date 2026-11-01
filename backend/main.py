from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="PROJECT NEXUS",
    description="AI Central Command for EVORA GROUP",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "project": "PROJECT NEXUS",
        "company": "EVORA GROUP",
        "founder": "XANDER LOW",
        "status": "ONLINE",
        "message": "NEXUS AI Central Command is ready",
        "time": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "system": "PROJECT NEXUS"
    }

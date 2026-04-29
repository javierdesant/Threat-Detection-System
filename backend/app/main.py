"""
Threat Detection System — FastAPI Backend

Entry point for the API server.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router

app = FastAPI(
    title="Threat Detection System API",
    description="Backend API for the edge-computing threat detection sensor network.",
    version="0.1.0",
)

# CORS — allow the React dev server during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")


@app.get("/", tags=["root"])
async def root():
    """Health-check / landing endpoint."""
    return {"message": "Threat Detection System API is running."}

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.routes import router as inventory_router
import os

app = FastAPI(title="Inventory Summary Tool")

# Include API routes
app.include_router(inventory_router, prefix="/inventory-summary")

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at the root URL
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

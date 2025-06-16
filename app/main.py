from fastapi import FastAPI
from app.api.routes import router as inventory_router

app = FastAPI(title="Inventory Summary Tool")

app.include_router(inventory_router, prefix="/inventory-summary")

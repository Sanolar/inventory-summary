from fastapi import APIRouter
from app.services.inventory import get_inventory, update_item  # inventory logic
from app.services.record_sales import record_sale  # sales logic
from app.schemas import ItemUpdate, SaleRequest  # ✅ all request schemas

router = APIRouter()

@router.get("/")
def view_inventory():
    return get_inventory()

@router.post("/update")
def modify_inventory(item: ItemUpdate):
    return update_item(item)

@router.post("/sale")
def make_sale(request: SaleRequest):
    return record_sale(request)

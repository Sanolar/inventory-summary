from pydantic import BaseModel
from typing import List

class ItemUpdate(BaseModel):
    name: str
    quantity: int
    price: float

class SaleItem(BaseModel):
    name: str
    quantity: int

class SaleRequest(BaseModel):
    items: List[SaleItem]

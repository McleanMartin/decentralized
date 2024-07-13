from pydantic import BaseModel, Field
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

class TenantSchema(BaseModel):
    id: Optional[int] = None
    name: str
    address: str

class ProductSchema(BaseModel):
    id: Optional[int] = None
    tenant_id: int
    name: str
    price: Decimal
    stock: int

class OrderItemSchema(BaseModel):
    id: Optional[int] = None
    order_id: int
    product_id: int
    quantity: int
    price: Decimal

class OrderSchema(BaseModel):
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    tenant_id: int
    total_amount: Decimal
    items: Optional[List[OrderItemSchema]] = []

class DeliverySchema(BaseModel):
    id: Optional[int] = None
    order_id: int
    address: str
    delivered: bool
    delivery_date: Optional[datetime] = None

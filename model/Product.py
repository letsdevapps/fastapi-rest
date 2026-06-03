from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=3, max_length=100)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)
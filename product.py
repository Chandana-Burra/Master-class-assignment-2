from pydantic import BaseModel
class Product(BaseModel):
    product_id: int
    name: str
    price: float
    category: str

from fastapi import FastAPI, HTTPException
from product import Product
from service import ProductService
app = FastAPI(title="Products API")
product_service= ProductService()
@app.post("/products", status_code=201)
def create_product(product: Product):
    result = product_service.add_product(product)
    if not result:
        raise HTTPException(status_code=400, detail="Product already exists")
    return result
@app.get("/products")
def read_products():
    return product_service.get_all_products()
@app.get("/products/{product_id}")
def read_product(product_id: int):
    product = product_service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    if product_id != product.product_id:
        raise HTTPException(status_code=400, detail="Product ID mismatch")
    success = product_service.update_product(product)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product updated successfully"}
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    success = product_service.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}

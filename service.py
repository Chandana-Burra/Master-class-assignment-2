from product import Product
from repo import product_store
class Service:
    def add_product(self, product: Product):
        for item in product_store:
            if item.product_id == product.product_id:
                return None
        product_store.append(product)
        return product
    def get_all_products(self):
        return product_store
    def get_product(self, product_id: int):
        for product in product_store:
            if product.product_id == product_id:
                return product
        return None
    def update_product(self, updated_product: Product):
        for index, product in enumerate(product_store):
            if product.product_id == updated_product.product_id:
                product_store[index] = updated_product
                return True
        return False
    def delete_product(self, product_id: int):
        for product in product_store:
            if product.product_id == product_id:
                product_store.remove(product)
                return True
        return False

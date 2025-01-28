from typing import List, Dict
from products import dao

class Product:
    def _init_(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    def load(data: Dict) -> 'Product':
        return Product(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            cost=data['cost'],
            qty=data.get('qty', 0)
        )
def list_products() -> List[Product]:
    return [Product.load(product) for product in dao.list_products()]
def get_product(product_id: int) -> Product:
    product_data = dao.get_product(product_id)
    if not product_data:
        raise ValueError(f"Product with ID {product_id} not found.")
    return Product.load
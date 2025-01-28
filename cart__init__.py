import json
import products
from cart import dao
from products import Product


class Cart:
    def _init_(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents  # List of Product instances
        self.cost = cost


    def load(data):
        # Static method for creating a Cart instance from data
        return Cart(data['id'], data['username'], data['contents'], data['cost'])
def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    items = []
    for cart_detail in cart_details:
        try:
            contents = json.loads(cart_detail['contents'])  # Replaced eval with json.loads
            items.extend(contents)
        except json.JSONDecodeError:
            print(f"Error decoding cart contents for user {username}.")
            continue

    return [products.get_product(item) for item in items]
def add_to_cart(username: str, product_id: int):
    try:
        dao.add_to_cart(username, product_id)
    except Exception as e:
        print(f"Error adding product {product_id} to cart for user {username}: {e}")
def remove_from_cart(username: str, product_id: int):
    try:
        dao.remove_from_cart(username, product_id)
    except Exception as e:
        print(f"Error removing product {product_id} from cart for user {username}: {e}")

def delete_cart(username: str):
    try:
        dao.delete_cart(username)
    except Exception as e:
        print(f"Error deleting cart for user {username}: {e}")
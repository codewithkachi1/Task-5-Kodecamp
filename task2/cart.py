import math
import json

class Cart:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, quantity, products):
        product = next((p for p in products if p.id == product_id), None)
        if product:
            if product_id in self.products:
                self.products[product_id]["quantity"] += quantity
            else:
                self.products[product_id] = {"product": product.to_dict(), "quantity": quantity}
        else:
            raise ValueError("Product not found")

    def checkout(self):
        total_cost = sum(item["product"]["price"] * item["quantity"] for item in self.products.values())
        rounded_cost = round(total_cost, 2)
        return rounded_cost

    def save_to_json(self, filename):
        cart_data = [{"product_id": pid, "quantity": item["quantity"]} for pid, item in self.products.items()]
        with open(filename, 'w') as f:
            json.dump(cart_data, f)

    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as f:
                cart_data = json.load(f)
                for item in cart_data:
                    self.products[item["product_id"]] = {"quantity": item["quantity"]}
        except FileNotFoundError:
            pass

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from product import Product
from cart import Cart

app = FastAPI()

# Sample products
products = [Product(1, "Product 1", 10.99), Product(2, "Product 2", 5.49)]

class CartRequest(BaseModel):
    product_id: int
    quantity: int

cart = Cart()
cart.load_from_json("cart.json")

@app.get("/products/")
def get_products():
    return [product.to_dict() for product in products]

@app.post("/cart/add")
def add_to_cart(request: CartRequest):
    try:
        cart.add_product(request.product_id, request.quantity, products)
        cart.save_to_json("cart.json")
        return {"message": "Product added to cart"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.get("/cart/checkout")
def checkout_cart():
    total_cost = cart.checkout()
    return {"total_cost": total_cost}

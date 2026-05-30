products = [
    {"name": "Coffee", "price": 120.00, "stock": 50},
    {"name": "Tea", "price": 80.00, "stock": 30},
    {"name": "Juice", "price": 150.00, "stock": 20}
]

for index, product in enumerate(products, start=1):
    print(f"Product: {product['name']} | Price: ₱{product['price']:.2f} | Stock: {product['stock']} units")
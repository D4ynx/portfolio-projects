products = [
    {'name': 'Coffee', 'price': 120.00},
    {'name': 'Tea', 'price': 80.00},
    {'name': 'Juice', 'price': 150.00}
]

def apply_discount(product, discount):
    discount_decimal = discount / 100
    discounted_price = product['price'] * (1 - discount_decimal)
    return {
        "name": product['name'],
        "original_price": product['price'],
        "discounted_price": discounted_price
    }

for product in products:
    discounted = apply_discount(product, 10)
    print(f"{discounted['name']}: ₱{discounted['original_price']:.2f} → ₱{discounted['discounted_price']:.2f}")
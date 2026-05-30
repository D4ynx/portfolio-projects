item_prices = [120.00, 80.00, 150.00, 50.00, 100.00]

for index, x in enumerate(item_prices, start=1):
    print(f"Item {index}: ₱{x:.2f}")
    
total = sum(item_prices)
print (f"The sum is ₱{total:,.2f}")
print (f"The average is ₱{total/len(item_prices):.2f}")
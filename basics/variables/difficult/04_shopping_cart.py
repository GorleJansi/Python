# Items with prices
cart = [200, 150, 50]  # total = 400

total = sum(cart)

# Discount logic: 10% off if total > 300
if total > 300:
    discount = total * 0.1 
    total -= discount
    print(f"Discount Applied: {discount}")

print(f"Final Total: {total}")

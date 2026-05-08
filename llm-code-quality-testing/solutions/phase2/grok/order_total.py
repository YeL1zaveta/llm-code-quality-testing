def calculate_order_total(items, discount_code):
    if not isinstance(items, list) or len(items) == 0:
        return False
    subtotal = 0.0
    for item in items:
        if not isinstance(item, dict):
            return False
        if not all(key in item for key in ['name', 'price', 'quantity']):
            return False
        price = item['price']
        quantity = item['quantity']
        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
            return False
        if price < 0 or quantity < 0:
            return False
        subtotal += price * quantity
    shipping = 0 if subtotal >= 200 else 15
    if discount_code == "SAVE10":
        discounted_subtotal = subtotal * 0.9
    else:
        discounted_subtotal = subtotal
    total = discounted_subtotal + shipping
    return total
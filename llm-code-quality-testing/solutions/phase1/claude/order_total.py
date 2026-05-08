def calculate_order_total(items, discount_code=None):
    if items is None or not isinstance(items, list) or len(items) == 0:
        return False

    total = 0
    for item in items:
        if not isinstance(item, dict):
            return False
        if not all(key in item for key in ('name', 'price', 'quantity')):
            return False
        if not isinstance(item['name'], str):
            return False
        if not isinstance(item['price'], (int, float)) or isinstance(item['price'], bool):
            return False
        if not isinstance(item['quantity'], int) or isinstance(item['quantity'], bool):
            return False
        if item['price'] < 0 or item['quantity'] < 0:
            return False
        total += item['price'] * item['quantity']

    if discount_code == "SAVE10":
        total *= 0.9

    if total < 200:
        total += 15

    return round(total, 2)
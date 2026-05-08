def calculate_order_total(items, discount_code):
    # Validate items
    if items is None or not isinstance(items, list) or len(items) == 0:
        return False

    total = 0

    for item in items:
        if not isinstance(item, dict):
            return False

        if not all(key in item for key in ["name", "price", "quantity"]):
            return False

        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        if not isinstance(name, str):
            return False
        if not (isinstance(price, (int, float)) and isinstance(quantity, int)):
            return False
        if price < 0 or quantity < 0:
            return False

        total += price * quantity

    # Apply discount
    if discount_code == "SAVE10":
        total *= 0.9

    # Apply shipping
    if total < 200:
        total += 15

    return total
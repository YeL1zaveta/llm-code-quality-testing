def calculate_order_total(items, discount_code=None):
    if items is None or not isinstance(items, list) or len(items) == 0:
        return False

    subtotal = 0.0

    for item in items:
        if not isinstance(item, dict):
            return False

        # Check for missing keys and valid data types
        if not all(k in item for k in ("name", "price", "quantity")):
            return False

        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        if not isinstance(name, str):
            return False
        if not isinstance(price, (int, float)) or not isinstance(quantity, int):
            return False

        # Check for negative values
        if price < 0 or quantity < 0:
            return False

        subtotal += price * quantity

    # Apply discount
    if discount_code == "SAVE10":
        subtotal *= 0.90

    # Determine shipping (based on total after discount)
    shipping = 0 if subtotal >= 200 else 15

    return subtotal + shipping
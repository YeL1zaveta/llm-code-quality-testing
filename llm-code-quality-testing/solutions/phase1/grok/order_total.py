def calculate_order_total(items, discount_code):
    if items is None or not isinstance(items, list) or len(items) == 0:
        return False

    total = 0.0

    for item in items:
        if not isinstance(item, dict):
            return False

        if "name" not in item or "price" not in item or "quantity" not in item:
            return False

        price = item["price"]
        quantity = item["quantity"]

        if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
            return False

        if price < 0 or quantity < 0:
            return False

        # quantity should ideally be integer, but we'll allow numeric
        total += price * quantity

    # Apply discount if valid
    if discount_code == "SAVE10":
        total *= 0.9

    # Add shipping
    shipping = 0 if total >= 200 else 15
    final_total = total + shipping

    return round(final_total, 2)
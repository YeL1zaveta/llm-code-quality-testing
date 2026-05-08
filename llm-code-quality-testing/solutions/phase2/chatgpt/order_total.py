def calculate_order_total(items, discount_code):
    # Validate items is a list
    if not isinstance(items, list):
        return None

    original_total = 0.0

    for item in items:
        # Validate each item is a dictionary
        if not isinstance(item, dict):
            return None

        # Check required keys
        if not all(k in item for k in ("name", "price", "quantity")):
            return None

        name = item["name"]
        price = item["price"]
        quantity = item["quantity"]

        # Validate data types
        if not isinstance(name, str):
            return None
        if not (isinstance(price, (int, float)) and isinstance(quantity, (int, float))):
            return None

        # Validate non-negative values
        if price < 0 or quantity < 0:
            return None

        original_total += price * quantity

    # Determine shipping cost
    shipping_cost = 0 if original_total >= 200 else 15

    # Apply discount if applicable
    discounted_total = original_total
    if discount_code == "SAVE10":
        discounted_total *= 0.9

    final_total = discounted_total + shipping_cost

    return round(final_total, 2)
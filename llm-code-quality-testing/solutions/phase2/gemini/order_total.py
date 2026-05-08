def calculate_order_total(items, discount_code):
    if not isinstance(items, list):
        return False

    if not items:
        return 0.0

    original_product_total = 0.0

    for item in items:
        if not isinstance(item, dict):
            return False

        # Check for required keys and valid types/values
        try:
            price = item['price']
            quantity = item['quantity']

            if not isinstance(price, (int, float)) or not isinstance(quantity, (int, float)):
                return False

            if price < 0 or quantity < 0:
                return False

            original_product_total += (price * quantity)
        except KeyError:
            return False

    # Apply discount logic
    discounted_total = original_product_total
    if discount_code == "SAVE10":
        discounted_total *= 0.9

    # Calculate shipping based on original total
    shipping = 0.0 if original_product_total >= 200 else 15.0

    return discounted_total + shipping
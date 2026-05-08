def calculate_order_total(items, discount_code):
    if not isinstance(items, list) or not items:
        return 0

    products_total = 0
    for item in items:
        if not isinstance(item, dict):
            continue
        try:
            price = float(item["price"])
            quantity = int(item["quantity"])
        except (KeyError, TypeError, ValueError):
            continue
        if price < 0 or quantity < 0:
            continue
        products_total += price * quantity

    if products_total == 0:
        return 0

    shipping = 0 if products_total >= 200 else 15

    if discount_code == "SAVE10":
        products_total *= 0.9

    return round(products_total + shipping, 2)
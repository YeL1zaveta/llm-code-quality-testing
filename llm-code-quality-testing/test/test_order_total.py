#from solutions.phase1.grok.order_total import calculate_order_total
#from solutions.phase1.claude.order_total import calculate_order_total
#from solutions.phase1.chatgpt.order_total import calculate_order_total
from solutions.phase1.gemini.order_total import calculate_order_total


#from solutions.phase2.grok.order_total import calculate_order_total
#from solutions.phase2.claude.order_total import calculate_order_total
#from solutions.phase2.chatgpt.order_total import calculate_order_total
#from solutions.phase2.gemini.order_total import calculate_order_total

def test_order_without_discount_below_free_shipping():
    items = [{"name": "Book", "price": 50, "quantity": 2}]
    assert calculate_order_total(items, None) == 115

def test_order_with_discount_below_free_shipping():
    items = [{"name": "Book", "price": 50, "quantity": 2}]
    assert calculate_order_total(items, "SAVE10") == 105

def test_order_with_invalid_discount_code():
    items = [{"name": "Book", "price": 50, "quantity": 2}]
    assert calculate_order_total(items, "INVALID") == 115

def test_order_with_discount_and_free_shipping():
    items = [{"name": "Book", "price": 100, "quantity": 2}]
    assert calculate_order_total(items, "SAVE10") == 180

def test_order_without_discount_and_free_shipping():
    items = [{"name": "Book", "price": 100, "quantity": 2}]
    assert calculate_order_total(items, None) == 200

def test_order_with_multiple_items_and_free_shipping():
    items = [
        {"name": "Book", "price": 100, "quantity": 2},
        {"name": "Book2", "price": 70, "quantity": 3},
    ]
    assert calculate_order_total(items, None) == 410

def test_invalid_items_type():
    assert calculate_order_total(None, None) == False

def test_order_with_negative_price():
    items = [{"name": "Book", "price": -100, "quantity": 2}]
    assert calculate_order_total(items, None) == False

def test_order_with_negative_quantity():
    items = [{"name": "Book", "price": 100, "quantity": -2}]
    assert calculate_order_total(items, None) == False

def test_order_without_quantity():
    items = [{"name": "Book", "price": 100}]
    assert calculate_order_total(items, None) == False

def test_order_without_price():
    items = [{"name": "Book", "quantity": 2}]
    assert calculate_order_total(items, None) == False

def test_order_empty_list():
    assert calculate_order_total([], None) == False
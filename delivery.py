FREE_SHIPPING_LIMIT = 50000
TEST_ORDER_PRICE = 50000

def is_free_shipping(order_price):
    return order_price >= FREE_SHIPPING_LIMIT

def get_delivery_message(order_price):
    if is_free_shipping(order_price):
        return "FREE_SHIPPING"
    return "DELIVERY_FEE_REQUIRED"

print(get_delivery_message(TEST_ORDER_PRICE))
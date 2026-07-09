FREE_SHIPPING_LIMIT = 50000
TEST_ORDER_PRICE = 50000

def get_delivery_message(order_price):
    message = "DELIVERY_FEE_REQUIRED"

    if order_price >= FREE_SHIPPING_LIMIT:
        message = "FREE_SHIPPING"

    return message

print(get_delivery_message(TEST_ORDER_PRICE))
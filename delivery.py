FREE_SHIPPING_LIMIT = 50000

def get_delivery_message(order_price):
    if order_price >= FREE_SHIPPING_LIMIT:
        return "FREE_SHIPPING"
    return "DELIVERY_FEE_REQUIRED"

print(get_delivery_message(50000))
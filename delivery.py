def get_delivery_message(order_price):
    if order_price >= 50000:
        return "FREE_SHIPPING"
    return "DELIVERY_FEE_REQUIRED"

print(get_delivery_message(50000))
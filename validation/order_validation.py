def validate_order_id(order_id):
    try:
        order_id = int(order_id)
    except (ValueError, TypeError):
        return False

    return order_id > 0

def validate_quantity(quantity):
    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        return False

    return quantity > 0

def validate_order_status(status):

    all_status = ["Pending", "Completed", "Cancelled"]

    if status in all_status:
        return True

    return False


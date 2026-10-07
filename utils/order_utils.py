from utils import file_handling
def get_orders():
    return file_handling.read_data("database/orders.json")

def get_next_order_id():
    data = get_orders()

    if data:
        next_order_id = max(order["order_id"] for order in data) + 1
        return next_order_id
    return 1

def find_order_by_id(order_id):
    data = get_orders()

    if not data:
        return None

    for order in data:
        if order["order_id"] == order_id:
            return order

    return None

def get_orders_by_table(table_id):
    data = get_orders()

    if not data:
        return []

    orders = []

    for order in data:
        if order["table_id"] == table_id:
            orders.append(order)

    return orders


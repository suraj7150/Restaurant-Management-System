from utils import menu_utils
from utils import file_handling

from utils import menu_utils


def calculate_subtotal(items):

    subtotal = 0

    for order_item in items:

        item = menu_utils.find_item_by_id(
            order_item["item_id"]
        )

        if item:
            subtotal += item["price"] * order_item["quantity"]

    return subtotal

def calculate_tax(subtotal):

    return subtotal*5/100

def calculate_discount(subtotal):

    subtotal = int(subtotal)

    if subtotal < 1000:
        return 0
    
    elif subtotal < 2000:
        return subtotal*5/100

    else:
        return subtotal*10/100

def calculate_final_amount(subtotal, tax, discount):

    return subtotal + tax - discount

def get_next_bill_id():

    data = file_handling.read_data("database/bills.json")

    if data:
        new_id = max(bill["bill_id"] for bill in data) + 1
    else :
        new_id = 1

    return new_id

def found_bill(bill_id):
    
    data = file_handling.read_data("database/bills.json")

    for bill in data:
        if bill["bill_id"] == bill_id:
            return bill

    return None
            




        
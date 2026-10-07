from utils import file_handling
from validation import item_validation

def get_name():

    while True:

        name = input("\t Enter item name : ")
        if item_validation.validate_item_name(name):
            return name
        else:
            print("\t Invalid Item Name ...")

def get_category():

    while True:

        category = input("\t Enter Item category : ")
        if item_validation.validate_category(category):
            return category
        else:
            print("\t Invalid Item category ...")

def get_price():

    while True:

        price = input("\t Enter Item price : ₹")
        if item_validation.validate_price(price):
            return float(price)
        else:
            print("\t Invalid Item price ...")


def find_item_by_id(item_id):

    data = file_handling.read_data(
        "database/menu.json"
    )

    if not data:
        return None

    for item in data:

        if item["id"] == item_id:
            return item

    return None
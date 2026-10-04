import re
def validate_item_name(name):
    name = str(name).strip()

    if not name:
        return False

    if not( 3<=len(name)<50):
        return False

    if not(re.fullmatch(r"[A-Za-z]+(?:[A-Za-z]+)*",name)):
        return False

    return True

def validate_category(category):

    category = str(category).strip()

    if not category:
        return False

    if not(re.fullmatch(r"[A-Za-z]+(?:[A-Za-z]+)*",category)):
        return False

    return True        

def validate_price(price):

    try:
        price = float(price)
        
        if price > 2000:
            return False
        
    except(ValueError,TypeError):
        return False

    return price > 0
        

def validate_id(item_id):

    try:
        item_id = int(item_id)
    except(ValueError, TypeError):
        return False

    return item_id > 0
    


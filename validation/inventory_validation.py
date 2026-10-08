import re

def validate_stock_name(name):

    name = str(name).strip()

    if not name:
        return False

    if not (2 <= len(name) < 50):
        return False

    if not re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", name):
        return False

    return True


def validate_category(category):

    category = str(category).strip()

    if not category:
        return False

    if not re.fullmatch(r"[A-Za-z]+(?: [A-Za-z]+)*", category):
        return False

    return True


def validate_unit(unit):

    unit = str(unit).strip().lower()

    valid_units = [
        "kg",
        "gram",
        "litre",
        "ml",
        "piece",
        "packet",
        "bottle",
        "dozen"
    ]

    return unit in valid_units


def validate_id(stock_id):

    try:
        stock_id = int(stock_id)
    except (ValueError, TypeError):
        return False

    return stock_id > 0
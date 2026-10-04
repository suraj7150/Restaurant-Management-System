import re

def validate_name(name):
    name =  str(name).strip()

    if not name:
        return False

    if not (3 <= len(name) < 50):
        return False

    if not re.fullmatch(r"[A-Za-z]+", name.replace(" ", "")):
        return False

    return True

def validate_email(email):

    email = str(email).strip()

    series = r"[A-Za-z0-9._%+-]+@[A-Za-z.-]+\.[A-Za-z]{2,}"

    if not email:
        return False

    if not re.fullmatch(series, email):
        return False

    return True

def validate_password(password):

    if not password:
        return False

    if(
         not ((re.search(r"[A-Z]", password)
        and re.search(r"[a-z]", password)
        and re.search(r"[0-9]", password)
        and re.search(r"[!@#$%^&*]", password)
        and len(password) >= 8))
    ):

        return False
    
    return True
    
def validate_phone_number(phone):

    phone = str(phone).strip()

    if not phone:
        return False

    if not (re.fullmatch(r"[6-9][0-9]{9}", phone)):
        return False

    return True

def validate_id(staff_id):

    try:
        staff_id = int(staff_id)
    except (ValueError, TypeError):
        return False

    return staff_id > 0

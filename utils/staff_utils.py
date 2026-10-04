import stdiomask
from validation import user_validation
def get_name():

    while True:
        name = input("\t Enter Name : ")

        if user_validation.validate_name(name):
            return name.strip()
        else :
            print("\t Invalid Name...!")

def get_email():

    while True:
        email = input("\t Enter Email : ")

        if user_validation.validate_email(email):
            return email.strip()
        else :
            print("\t Invalid Email...!")

def get_password():

    while True:
        password = stdiomask.getpass(
            "\t Enter Password : ", 
            mask="*"
        )

        if user_validation.validate_password(password):
            return password
        else :
            print("\t Invalid Password...!")

def get_phone():

    while True:
        phone = input("\t Enter Phone Number : ")

        if user_validation.validate_phone_number(phone):
            return phone.strip()
        else :
            print("\t Invalid Phone Number...!")








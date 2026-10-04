import stdiomask
from validation import user_validation
from utils.logger import logger
from utils import file_handling
from table.table_booking import TableBooking

class Staff:
    def __init__(self):
        # self.table_booking = TableBooking()
        pass

    def authentication(self):
            
        try:
            while True:
                while True:
                
                    email = input("\t Enter your email   : ")

                    if user_validation.validate_email(email):
                        break
                    else:
                        logger.warning("Invalid staff email format entered")
                        print("\t Invalid Email! ...")

                while True:

                    password = stdiomask.getpass(
                        "\t Enter your password  : ",
                        mask="*"
                    )

                    if user_validation.validate_password(password):
                        break
                    else:
                        logger.warning("Invalid staff password format entered")
                        print("\t Invalid Password! ...")

                data = file_handling.read_data("database/user.json")

                staff_data = data["staff"]

                found = False

                for staff_id in staff_data:
                    if(
                        email == staff_id["email"] and 
                        password == staff_id["password"]
                    ):
                        logger.info("Staff login successful")
                        print("\t Login successfully...")
                        self.staff_menu()
                        found = True
                        break

                    else:
                        logger.warning("Invalid staff credentials")
                        print("\t Staff not found...")

                if found:
                    break
        except Exception as error:

            logger.error(
                f"Error during staff authentication: {error}"
            )

            print(f"\t Error: {error}") 

    def staff_menu(self):

        try:
            while True:
                print("\n" + "\t" + "‗" * 50)
                print("\n\t          STAFF DASHBOARD")
                print("\t" + "‗" * 50)

                print("\n\t\t 1  ->  Order Management")
                print("\t\t 2  ->  Table Booking")
                print("\t\t 3  ->  Logout")

                print("\t" + "‗" * 50)

                option = input("\n\t Please select your choice (1-3): ")

                if option == "1":
                    logger.info(
                        "Staff selected Order Management"
                    )
                    print("\n\t" + "=" * 50)
                    print("\t\t  Order Management")
                    print("\t" + "=" * 50)

                elif option == "2":
                    logger.info(
                        "Staff selected Table Booking"
                    )
                    # self.table_booking.booking_menu()
                    TableBooking().booking_menu()
                    

                elif option == "3":
                    logger.info(
                        "Staff logout"
                    )
                    print("\n\t" + "=" * 50)
                    print("\t\t  Staff Logout")
                    print("\t" + "=" * 50)
                    break

                else:
                    logger.warning(
                        f"Invalid staff menu option: {option}"
                    )
                    print("\n\t\t  Invalid option!")

        except Exception as error:

            logger.exception(
                f"Unexpected error in staff dashboard: {error}"
            )

            print(f"\n\t Error: {error}")
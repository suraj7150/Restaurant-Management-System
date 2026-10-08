import stdiomask
from validation import user_validation
from inventory.inventory import Inventory
from menu.menu_manager import MenuManager
from staff.staff_management import StaffManagement
from table.table_management import TableManagement
from utils import file_handling
from utils.logger import logger

class Admin:

    def __init__(self):
        self.menu_manager = MenuManager()
        self.inventory_manager = Inventory()
        self.staff_management = StaffManagement()
        self.table_management = TableManagement()


    def authentication(self):

        try:
            while True:
                while True:

                    email = input("\t Enter your email : ")

                    if user_validation.validate_email(email) :
                        break
                    else:
                        logger.warning("Invalid email format entered")
                        print("\t Invalid Email! ...")

                while True:

                    password = stdiomask.getpass(
                        "\t Enter your password : ", 
                        mask="*"
                    )

                    if user_validation.validate_password(password):
                        break
                    else:
                        logger.warning("Invalid password format entered")
                        print("\t Invalid Password! ...")

                data = file_handling.read_data("database/user.json")
                admin_data = data["admin"]

                if (
                    email == admin_data["email"] and
                    password == admin_data["password"] 
                ):
                    logger.info("Admin login successful")

                    print("\t Login successfully...")
                    self.admin_menu()
                    break
                    
                else:
                    logger.warning("Invalid admin credentials")
                    print("\t Admin not found...")

        except Exception as error:
            logger.error(
                f"Error while in admin login : {error}"
            )
            print(f"Error : {error}")
            

    def admin_menu(self):
        
        try:
            while True:
                print("\n" + "\t" + "‗" * 50)
                print("\n\t         ADMIN DASHBOARD")
                print("\t" + "‗" * 50)

                print("\n\t\t 1  →  Inventory Management")
                print("\t\t 2  →  Staff Management")
                print("\t\t 3  →  Order Management")
                print("\t\t 4  →   Menu Management")
                print("\t\t 5  →  Table Management")
                print("\t\t 6  →  Logout")
                print("\t" + "‗" * 50)

                option = input("\n\t please select any option (1-6) : ")

                if option == "1":
                    logger.info(
                        "Admin selected Inventory Management"
                    )
                    self.inventory_manager.inventory_menu()

                elif option == "2":
                    logger.info(
                        "Admin selected Staff Management"
                    )
                    self.staff_management.staff_menu()

                elif option == "3":
                    logger.info(
                        "Admin selected Order Management"
                    )
                    print("\n\t" + "‗" * 50)
                    print("\n\t\t  Order Management")
                    print("\t" + "‗" * 50)

                elif option == "4":
                    logger.info(
                        "Admin selected Menu Management"
                    )
                    self.menu_manager.menu_menu()

                elif option == "5":
                    logger.info(
                        "Admin selected Table Management"
                    )
                    self.table_management.management_menu()

                elif option == "6":
                    logger.info("Admin logout successful")
                    print("\n\t\t  Admin Logout..")
                    break

                else:
                    logger.warning(
                        f"Invalid admin menu option entered: {option}"
                    )

                    print("\n\t\t Invalid option!...")

        except Exception as error:
            logger.error(
                f"Error while in admin dashboard : {error}"
            )
            print(f"Error : {error}")
                

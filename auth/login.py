from . import admin
from . import staff
from utils.logger import logger

class Login:
    def __init__(self):
        pass

    def login_menu(self):
        try:
            while True:
                print("\n" + "\t" + "‗" * 50)
                print("\n\t         RESTAURANT MANAGEMENT ")
                print("\t" + "‗" * 50)
                print("\n\t\t 1  -> Admin Login")
                print("\t\t 2  -> Staff Login")
                print("\t\t 3  -> Exit")
                print("\t" + "‗" * 50)


                option = input("\n\t please select your choice (1-3) : ")

                if option == "1":

                    print("\n\t" + "‗" * 50)
                    print("\n\t\t  Admin Login")
                    print("\t" + "‗" * 50)

                    admin.Admin().authentication()

                elif option == "2":

                    print("\n\t" + "‗" * 50)
                    print("\n\t\t  Staff Login")
                    print("\t" + "‗" * 50)

                    staff.Staff().authentication()

                elif option == "3":
                    logger.info("Admin logout successful")
                    
                    print("\n\t Thank you! visit again...")
                    break
                else:
                    logger.warning(
                        f"Invalid login menu option entered: {option}"
                    )
                    print("\t Invalid option...!")
        
        except Exception as error:
            logger.error(
                f"Error while login user : {error}"
            )
            print(f"\n\tError: {error}")
         
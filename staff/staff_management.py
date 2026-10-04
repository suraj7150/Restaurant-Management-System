from utils import file_handling
from staff.add_staff import AddStaff
from staff.delete_staff import DeleteStaff
from utils.logger import logger

class StaffManagement:

    def staff_menu(self):
            
        try:
            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t  Staff Management")
                print("\t" + "‗" * 50)
                print("\n\t\t 1  ->   Add Staff")
                print("\t\t 2  ->   Delete Staff")
                print("\t\t 3  ->   View Staff")
                print("\t\t 4  ->   Back")

                print("\t" + "‗" * 50)

                option = input("\t select any option in given menu : ")

                if option == "1":
                    logger.info("Opening Add Staff")
                    AddStaff().add_staff()

                elif option == "2":
                    logger.info("Opening Delete Staff")
                    DeleteStaff().delete_staff()

                elif option == "3":
                    logger.info("Opening View Staff")
                    self.view_staff()

                elif option == "4":
                    logger.info("Exiting Staff Management")
                    break

                else:
                    logger.warning(
                        f"Invalid staff menu option: {option}"
                    )
                    print("Invalid option ...")

        except Exception as error:
            logger.error(
                f"Error while in staff management menu : {error}"
            )
            print(f"Error : {error}")

    def view_staff(self):

        try:
            user_data = file_handling.read_data("database/user.json")
            
            data = user_data["staff"]

            print("‗" * 80)
            print("\n                      STAFF MANAGEMENT")
            print("‗" * 80)

            print(
                f'\n{"ID   "}'
                f'{"NAME                "}'
                f'{"EMAIL                              "}'
                f'{"MOBILE"}'
            )
            print("‗" * 80)

            for staff in data:
                print(
                    f'{staff["id"]:<5}'
                    f'{staff["name"]:<20}'
                    f'{staff["email"]:<35}'
                    f'{staff["phone"]:<11}'
                )

            print("‗" * 80)

            logger.info("Staff data displayed successfully")

        except Exception as error:
            logger.error(
                f"Error while in view staff : {error}"
            )
            print(f"Error : {error}")

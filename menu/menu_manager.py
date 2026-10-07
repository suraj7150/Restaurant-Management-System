import json
from .add_item import AddItem
from utils import file_handling
from .update_item import UpdateItem
from .delete_item import DeleteItem
from utils.logger import logger

class MenuManager:

    def __init__(self):
        pass

    def menu_menu(self):
        
        try:
            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t   Menu Management")
                print("\t" + "‗" * 50)
                print("\n\t\t 1  →   Add Item")
                print("\t\t 2  →   View Items")
                print("\t\t 3  →   Update Item")
                print("\t\t 4  →   Delete Item")
                print("\t\t 5  →   Back")

                print("\t" + "‗" * 50)

                option = input("\t select any option in given menu : ")

                if option == "1":
                    logger.info("Opening Add Item")
                    AddItem().add_item()

                elif option == "2":
                    logger.info("Opening View Items")
                    self.show_item()

                elif option == "3":
                    logger.info("Opening Update Items")
                    UpdateItem().update_item()

                elif option == "4":
                    logger.info("Opening Delete Items")
                    DeleteItem().delete_item()

                elif option == "5":
                    logger.info("Exiting Menu Management")
                    break

                else:
                    logger.warning(f"Invalid menu option entered: {option}")
                    print("Invalid option ...")

        except Exception as error:
            logger.error(
                f"Error while in menu management : {error}"
            )
            print("Error : {error}")

    def show_item(self):

        try:
            data = file_handling.read_data("database/menu.json")
            if not data:
                logger.warning("No menu items found")
                print("\nNo menu items found.")
                return

            logger.info(f"Successfully loaded {len(data)} menu items")
            print("‗" * 50)
            print(f"\n               MAIN MENU  ")
            
            temp_category = None
            for item in data:

                if not temp_category == item["category"]:
                    temp_category = item["category"]
                    print("‗" * 50)
                    print(f'{item["category"].upper()}')
                    print("‗" * 50)
                    print(
                        f'{"ID":<8}'
                        f'{"NAME":<31}'
                        f'{"PRICE":<6}'
                    )
                else:
                    print(
                        f'{item["id"]:<8}'
                        f'{item["name"]:<31}'
                        f'₹{item["price"]:<6}'
                    )
                    
            print("‗" * 50)


        except Exception as error:
            logger.error(
                f"Error while Show Item : {error}"
            )
            print(f"Error : {error}")
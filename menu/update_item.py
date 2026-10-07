import json
from utils import menu_utils
from utils import file_handling
from validation import item_validation
from utils.logger import logger

class UpdateItem:

    def __init__(self):
        self.item_id = None
    
    def update_item(self):

        try:
            while True:

                self.item_id = int(input("\t Enter item id : "))

                if item_validation.validate_id(self.item_id):
                    self.item_id = int(self.item_id)
                    logger.info(
                        f"Valid item ID entered: {self.item_id}"
                    )
                    break
                else:
                    logger.warning(
                        f"Invalid item ID entered: {self.item_id}"
                    )
                    print("\t Invalid Id...!")

                
            data = file_handling.read_data("database/menu.json")

            for item in data:
                if item["id"] == self.item_id:
                    logger.info(
                        f"Item found for update: ID = {self.item_id}"
                    )

                    self.update_menu(item)

                    file_handling.write_data(
                        "database/menu.json",
                        data
                    )
                    return
                
            logger.warning(
                f"Item not found for update: ID = {self.item_id}"
            )
                
            print("\t This Item is not found...!")

        except Exception as error:
            logger.error(
                f"Error while in update item : {error}"
            )
            print(f"Error : {error}")

    def update_menu(self, item):

        try:
            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t 1  →   Update Name")
                print("\t\t 2  →   Update Category")
                print("\t\t 3  →   Update Price")
                print("\t\t 4  →   Back")
                print("\t" + "‗" * 50)

                option = input("select your choice(1-3) :")

                if option == "1":
                    logger.info("Update Name option selected")
                    self.update_name(item)
                    break

                elif option == "2":
                    logger.info("Update Category option selected")

                    self.update_category(item)
                    break

                elif option == "3":
                    logger.info("Update Price option selected")
                    self.update_price(item)
                    break

                elif option == "4":
                    logger.warning(
                        f"Invalid update menu option entered: {option}"
                    )
                    return
                
                else:
                    print("Invalid choice!...")

        except Exception as error:
            logger.error(
                f"Error while update menu : {error}"
            )
            print(f"Error : {error}")

    def update_name(self, item):

        name = menu_utils.get_name()

        item["name"] = name

        logger.info(
            f"Item name updated successfully: ID = {item['id']}"
        )

        print("\t Item Name Updated Successfully...!")

    def update_category(self, item):

        category = menu_utils.get_category()

        item["category"] = category

        logger.info(
            f"Item category updated successfully: ID = {item['id']}"
        )

        print("\t Item Category Updated Successfully...!")

    def update_price(self, item):

        price = menu_utils.get_price()

        item["price"] = price

        logger.info(
            f"Item price updated successfully: ID = {item['id']}"
        )
        
        print("\t Item Price Updated Successfully...!")

    


        
        
        
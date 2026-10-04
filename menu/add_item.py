from utils import menu_utils
from .main_item import MenuItem
from utils import file_handling
from utils.logger import logger

class AddItem:

    def __init__(self):
        self.name = None
        self.category = None
        self.price = None
        self.is_veg = None
        self.is_available = None

    def add_item(self):

        try:
            self.name = menu_utils.get_name()
            logger.info(f"Item name received: {self.name}")

            self.category = menu_utils.get_category()
            logger.info(f"Item category received: {self.category}")

            self.price = menu_utils.get_price()
            logger.info(f"Item price received: {self.price}")

            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t 1  ->   Veg")
                print("\t\t 2  ->   Non-Veg")
                print("\t" + "‗" * 50)

                option = input("\tEnter your choice (1-2) :")

                if option == "1":
                    self.is_veg = True
                    break
                elif option == "2":
                    self.is_veg = False
                    break
                else:
                    logger.warning(
                        f"Invalid Veg/Non-Veg option entered: {option}"
                    )
                    print("\tInvalid choice...")
                
            while True:
            
                print("\n\t" + "‗" * 50)
                print("\n\t\t1  ->   Available")
                print("\t\t2  ->   Not Available")
                print("\t" + "‗" * 50)

                option = input("\tEnter your choice (1-2) :")

                if option == "1":
                    self.is_available = True
                    break
                elif option == "2":
                    self.is_available = False
                    break
                else:
                    logger.warning(
                        f"Invalid availability option entered: {option}"
                    )
                    print("\tInvalid choice...")

            

            data = file_handling.read_data("database/menu.json")
            duplicate = False

            for item in data:
                if (
                    item["name"].strip().lower() == self.name.strip().lower()
                    and item["category"].strip().lower() == self.category.strip().lower()
                    and float(item["price"]) == self.price
                    and item["isVeg"] == self.is_veg
                    and item["isAvailable"] == self.is_available
                ):
                    logger.warning(
                        f"Duplicate item found: "
                        f"{self.name} - {self.category}"
                    )

                    print("This Item is already exist...")
                    duplicate = True
                    break

            if duplicate:
                logger.info("Add item operation stopped due to duplicate")
                return
            
            if data:
                item_id = max(item["id"] for item in data) + 1
            else:
                item_id = 1

            logger.info(f"Generated new item ID: {item_id}")

            new_item = MenuItem(
                item_id,
                self.name,
                self.category,
                self.price,
                self.is_veg,
                self.is_available
            )

            data.append(new_item.item_object())

            file_handling.write_data("database/menu.json", data)

            logger.info(
                f"Item added successfully: "
                f"ID={item_id}, Name={self.name}"
            )

            print("\n\t Item added successfully...!")
            print(f"\t Item ID : {item_id}")

        except Exception as error:
            logger.error(
                f"Error while in add item : {error}"
            )

            print(f"Error : {error}")
            
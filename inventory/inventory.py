from utils import file_handling
from validation import inventory_validation
from utils.logger import logger
class Inventory:

    def __init__(self):
        self.stock_id = None

    def inventory_menu(self):

        try:
            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t  Inventory Management")
                print("\t" + "‗" * 50)
                print("\n\t\t 1  ->   Add Stock")
                print("\t\t 2  ->   View Stock")
                print("\t\t 3  ->   Delete Stock")
                print("\t\t 4  ->   Back")

                print("\t" + "‗" * 50)

                option = input("\t select any option in given menu : ")

                if option == "1":
                    logger.info("Opening Add Stock")
                    self.add_stock()

                elif option == "2":
                    logger.info("Opening View Stock")
                    self.view_stock()

                elif option == "3":
                    logger.info("Opening Delete Stock")
                    self.delete_stock()

                elif option == "4":
                    logger.info("Exiting Inventory Management")
                    break

                else:
                    logger.warning(
                        f"Invalid inventory menu option: {option}"
                    )
                    
                    print("Invalid option ...")

        except Exception as error:
            logger.error(
                f"Error while inventory menu : {error}"
            )
            print(f"Error : {error}")

    def add_stock(self):

        try:
            while True:

                name = input("\t Enter stock name : ")
                if inventory_validation.validate_stock_name(name):
                    name = name.strip()

                    logger.info(
                        f"Valid stock name entered: {name}"
                    )

                    break 
                else :
                    logger.warning(
                        f"Invalid stock name entered: {name}"
                    )

                    print("\t Invalid stock name...!")

            while True:

                category = input("\t Enter stock category : ")
                if inventory_validation.validate_category(category):
                    category = category.strip()

                    logger.info(
                        f"Valid stock category entered: {category}"
                    )

                    break
                else:
                    logger.warning(
                        f"Invalid stock category entered: {category}"
                    )

                    print("\t Invalid stock category...!")

            while True:

                unit = input("\t Enter stock unit : ")
                if inventory_validation.validate_unit(unit):
                    unit = unit.strip().lower()

                    logger.info(
                        f"Valid stock unit entered: {unit}"
                    )

                    break
                else:
                    logger.warning(
                        f"Invalid stock unit entered: {unit}"
                    )

                    print("\t Invalid stock unit...!")

            data = file_handling.read_data(
                "database/inventory.json"
            )
            
            for stock in data:
                if (
                    stock["name"].strip().lower() == name.lower()
                    and stock["category"].strip().lower() == category.lower()
                    and stock["unit"].strip().lower() == unit.lower()
                ):
                    logger.warning(
                        f"Duplicate stock found: "
                        f"Name={name}, Category={category}, Unit={unit}"
                    )

                    print("\t This Stock already exists...!")
                    return

            if data:
                stock_id = max(stock["id"] for stock in data) + 1
            else:
                stock_id = 1

            logger.info(
                f"Generated new stock ID: {stock_id}"
            )

            new_stock = {
                "id": stock_id,
                "name": name,
                "category": category,
                "unit": unit
            }

            data.append(new_stock)

            file_handling.write_data(
                "database/inventory.json",
                data
            )

            logger.info(
                f"Stock added successfully: "
                f"ID={stock_id}, Name={name}"
            )

            print("\n\t Stock added successfully...!")
            print(f"\t Stock ID : {stock_id}")
        
        except Exception as error:
            logger.error(
                f"Error while add stock : {error}"
            )
            print(f"Error : {error}")

    def view_stock(self):

        try:

            data = file_handling.read_data("database/inventory.json")
            
            logger.info(
                f"Inventory data loaded successfully: "
                f"{len(data)} stock(s)"
            )
          
            print("‗" * 80)
            print(f"\n                   INVENTORY")
            print("‗" * 80)

            print(
                f'\n{"ID      "}'
                f'{"NAME                           "}'
                f'{"UNIT      "}'
                f'{"CATEGORY"}'
            )
            print("‗" * 80)

            for item in data:

                print(
                    f'{item["id"]:<8}'
                    f'{item["name"]:<31}'
                    f'{item["unit"]:<10}'
                    f'{item["category"]:<31}'
                )
            print("‗" * 80)

        except Exception as error:
            logger.error(
                f"Error while in view stock : {error}"
            )
            print(f"Error : {error}")

    def delete_stock(self):

        try:
            while True:
                self.stock_id = input("\t Enter Stock Id : ")
                
                if inventory_validation.validate_id(self.stock_id):

                    self.stock_id = int(self.stock_id)

                    logger.info(
                        f"Valid stock ID entered: {self.stock_id}"
                    )
                    break
                else:
                    logger.warning(
                        f"Invalid stock ID entered: {self.stock_id}"
                    )

                    print("\t Invalid Id...!")

            logger.info("Reading inventory data for deletion")

            data = file_handling.read_data("database/inventory.json")

            for stock in data:
                        
                if stock["id"] == self.stock_id:

                    data.remove(stock)
                    
                    file_handling.write_data(
                        "database/inventory.json",
                        data
                    )

                    logger.info(
                        f"Stock deleted successfully: "
                        f"ID={self.stock_id}"
                    )

                    print("\t Stock deleted successfully!")
                    return
                
            logger.warning(
                f"Stock not found for deletion: "
                f"ID={self.stock_id}"
            )
            print("\t This Stock is not found...!")

        except Exception as error:
            logger.error(
                f"Error while in delete stock : {error}"
            )
            print(f"Error : {error}")
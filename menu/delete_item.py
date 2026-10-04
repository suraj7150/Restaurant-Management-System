from validation import item_validation
from utils import file_handling
from utils.logger import logger

class DeleteItem:
    def __init__(self):
        self.item_id = None

    def delete_item(self):

        try:
            while True:
            
                self.item_id = input("\t Enter item id : ")

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

                    data.remove(item)
                    
                    file_handling.write_data(
                        "database/menu.json",
                        data
                    )

                    logger.info(
                        f"Item deleted successfully: "
                        f"ID = {self.item_id}"
                    )

                    print("\t Item deleted successfully!")
                    return
                
            logger.warning(
                f"Item not found for deletion: "
                f"ID = {self.item_id}"
            )
            
            print("\t This Item is not found...!")

        except Exception as error:
            logger.error(
                f"Error while in delete item : {error}"
            )
            print(f"Error : {error}")
        
        

        

from validation import table_validation
from utils import file_handling
from table import table
from utils.logger import logger
from exception.custom_exception import TableNotFoundException

class TableManagement:

    def __init__(self):
        pass

    def management_menu(self):
        while True:

            print("\n\t" + "‗" * 50)
            print("\n\t\t  TABLE Management")
            print("\t" + "‗" * 50)
            print("\n\t\t 1  →   Add Table")
            print("\t\t 2  →   View Table")
            print("\t\t 3  →   Delete Table")
            print("\t\t 4  →   Back")

            print("\t" + "‗" * 50)

            option = input("\t select any option in given menu : ")

            if option == "1":
                self.add_table()

            elif option == "2":
                self.view_table()

            elif option == "3":
                self.delete_table()

            elif option == "4":
                break

            else:
                print("Invalid option ...")

    def add_table(self):
        
            try:
                while True:
                    size = input("\t Enter table size : ")

                    if table_validation.validate_size(size):
                        size = int(size)
                        break
                    else:
                        print("\t Invalid Table Size...!")

                data = file_handling.read_data("database/tables.json")

                if data :
                    table_id = max(table["id"] for table in data) + 1
                else:
                    table_id = 1

                table_obj = table.Table()

                table_obj.id = table_id
                table_obj.size = size
                table_obj.status = "Available"

                table_obj.set_booking_start(None)
                table_obj.set_booking_duration(None)

                new_table = table_obj.table_object()
                data.append(new_table)

                file_handling.write_data(
                    "database/tables.json",
                    data
                )
                logger.info(
                    f"Table {table_id} Added Successfully..."
                )
                print("\t Table added successfully!")
                print(f"\t Table ID : {table_id}")

            except Exception as error:
                logger.error(
                    f"Error while adding table: {error}"
                )

                print("\t Unable to add table...!")


    def view_table(self):

        try: 

            data = file_handling.read_data("database/tables.json")
            if not data:
                logger.warning(
                    "No tables found in database."
                )
                print("\n\tNo tables available...!")
                return

            print("‗" * 80)
            print(f"\n                   TABLE MANAGEMENT")
            print("‗" * 80)

            print(
                f'{"ID":<6}'
                f'{"SEATS":<12}'
                f'{"STATUS":<15}'
                f'{"BOOKING START":<30}'
                f'{"DURATION":<30}'
            )
            print("‗" * 80)
            for table in data:
            
                if table["status"] == "Available":
                    booking_start = "-"
                    booking_duration = "-"
                else:
                    booking_start = table["booking_start"]
                    booking_duration = table["booking_duration"]

                print(
                    f'{table["id"]:<6}'
                    f'{table["size"]:<2}'
                    f'{"seats":<10}'
                    f'{table["status"]:<15}'
                    f'{str(booking_start):<30}'
                    f'{str(booking_duration):<5}'
                    f'{"hours":<10}'
                )

            print("‗" * 80)

            logger.info("Tables viewed successfully.")

        except Exception as error:
            logger.error(
                f"Error while in view table : {error}"
            )
            print("\tUnable to view tables...!")

    def delete_table(self):
            
        try:
            while True:
                table_id = input("\t Enter table id : ")

                if table_validation.validate_id(table_id):
                    table_id = int(table_id)
                    logger.info(
                        f"Valid Table ID entered: {table_id}"
                    )
                    break
                else:
                    logger.warning(
                        f"Invalid Table ID entered: {table_id}"
                    )
                    print("\t Invalid Table Id...!")

            data = file_handling.read_data("database/tables.json")

            for table in data:
                if table["id"] == table_id:

                    data.remove(table)

                    file_handling.write_data(
                        "database/tables.json",
                        data
                    )

                    logger.info(
                        f"Table deleted successfully: "
                        f"ID={table_id}"
                    )       
                    print("\t Table deleted successfully!")
                    return    

            raise TableNotFoundException(
                f"Table with ID {table_id} not found."
            )


        except TableNotFoundException as error:

            logger.warning(str(error))
            print("\t This Table is not found...!")
            
        except Exception as error:
            logger.error(
                f"Error while in delete table : {error}"
            )
            print("\t Unable to delete table...!")
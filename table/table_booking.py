from utils import file_handling
from utils.logger import logger
from validation import table_validation
from utils import table_utils
from utils import staff_utils
from datetime import datetime

class TableManager:

    def view_available_tables(self):

            try:

                data = file_handling.read_data("database/tables.json")

                if not data:
                    logger.warning(
                        "No tables found in database."
                    )
                    print("\n\tNo tables available...!")
                    return  
                
                available_tables = []

                for table in data:
                    if table.get("status") == "Available":
                        available_tables.append(table)

                if not available_tables:
                    logger.warning("No available tables found.")
                    print("\n\tNo tables available...!")
                    return

                logger.info(
                    f"Found {len(available_tables)} available table(s)."
                )
        

                print("\t" + "‗" * 40)
                print(f"\n\t       AVAILABLE TABLE")
                print("\t" + "‗" * 40)

                print(
                    f'\t\t{"ID":<6}'
                    f'{"TABLE SIZE":<15}'
                )
                print("\t" + "‗" * 40)

                for table in available_tables:
                    print(
                        f'\t\t{table["id"]:<6}'
                        f'{str(table["size"]) + " seats":<15}'
                    )
                print("\t" + "‗" * 40)

                logger.info("Available tables displayed successfully.")

            except Exception as error:
                logger.error(
                    f"Error while in view available tables : {error}"
                )
                print("\tUnable to view available tables...!")

        

class BookTable(TableManager):

    def __init__(self):
        pass

    def book_table(self):
        try:

            name = staff_utils.get_name()

            email = staff_utils.get_email()

            phone = staff_utils.get_phone()

            while True:
                customer_count = input("\t Enter number of customers : ")

                if table_validation.validate_customer_count(customer_count):
                    customer_count = int(customer_count)
                    logger.info(
                        f"Valid customer count entered: {customer_count}"
                    )
                    break
                else:
                    logger.warning(
                        f"Invalid customer count entered: {customer_count}"
                    )
                    print("\t Customer count must be greater than 0...!")

            is_multi = False

            if table_utils.get_available_tables():

                if table_utils.is_multiple_tables(customer_count):
                    is_multi = True 
            else:
                print("Tables not available...!")

            if is_multi:
                self.view_available_tables()
                suitable_tables = table_utils.get_multiple_tables(customer_count)
                if not suitable_tables:
                    print("Suitable tables not available...!")
                    return

                table_ids = [table["id"] for table in suitable_tables]

                duration = input("Enter booking duration (in hours) : ")
                while True:
                
                    if table_validation.validate_booking_duration(duration):
                        duration = int(duration)
                        data = file_handling.read_data("database/bookings.json")

                        booking_id = max(table["booking_id"] for table in data) + 1

                        booking_table = table_utils.booking_object( booking_id,
                            name, email, phone, customer_count, table_ids,
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            duration, "Active"
                        )
                        data.append(booking_table)
                        file_handling.write_data(
                            "database/bookings.json",
                            data
                        )
                        data = file_handling.read_data("database/tables.json")

                        selected_ids = [table["id"] for table in suitable_tables]
                        for table in data:
                            if table["id"] in selected_ids:
                                table["status"] = "Occupied"
                                table["booking_duration"] = duration
                                table["booking_start"] = datetime.now().strftime(
                                                            "%Y-%m-%d %H:%M:%S")      
                        file_handling.write_data(
                            "database/tables.json",
                            data
                        )
                        break

                    else:
                        print("Invalid duration...!")

            else:
                best_table, suitable_tables = table_utils.get_one_table(customer_count)

                for table in suitable_tables:
                    if table["size"] < customer_count:
                        suitable_tables.remove(table)

                print("\t" + "‗" * 30)
                print(f"\n\t       RECOMMEND TABLE")
                print("\t" + "‗" * 30)
                print(
                    f'\t Id             : {best_table["id"]}'
                    f'\n\t Seats          : {best_table["size"]}'
                    f'\n\t Total Customer : {customer_count}'
                )
                print("\t" + "‗" * 30)

                print("\t" + "‗" * 40)
                print(f"\n\t       SUITABLE TABLE")
                print("\t" + "‗" * 40)

                print(
                    f'\t\t{"ID":<6}'
                    f'{"TABLE SIZE":<15}'
                )
                print("\t" + "‗" * 40)
                for table in suitable_tables:
                    print(
                        f'\t\t{table["id"]:<6}'
                        f'{str(table["size"]) + " seats":<15}'
                    )
                print("\t" + "‗" * 40)

                while True:
                    table_id = input("\t\tEnter table id : ")

                    if table_validation.validate_id(table_id):
                        table_id = int(table_id)
                        break
                    else:
                        print("Invalid id...!")

                found = False
                for table in suitable_tables:
                    if table["id"] == table_id:
                        found = True
                if not found:
                    print("out of range table id...!")
                    return

                duration = input("Enter booking duration (in hours) : ")
                while True:

                    if table_validation.validate_booking_duration(duration):
                        duration = int(duration)
                        table_ids = []

                        table_ids.append(table_id)

                        data = file_handling.read_data("database/bookings.json")

                        booking_id = max(table["booking_id"] for table in data) + 1       

                        booking_table = table_utils.booking_object( booking_id,
                            name, email, phone, customer_count, table_ids,
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            duration, "Active"
                        )
                        data.append(booking_table)
                        file_handling.write_data(
                            "database/bookings.json",
                            data
                        )
                        data = file_handling.read_data("database/tables.json")
                        for table in data:
                            if table["id"] == table_id:
                                table["status"] = "Occupied"
                                table["booking_duration"] = duration
                                table["booking_start"] = datetime.now().strftime(
                                                            "%Y-%m-%d %H:%M:%S")
                                break
                        file_handling.write_data(
                            "database/tables.json",
                            data
                        )
                        break
                    else:
                        print("Invalid duration...!")
      
        except Exception as error:
            logger.error(
                f"Error while in book table : {error}"
            )
            print("\tUnable to book table...!")

class TableBooking(BookTable):

    def booking_menu(self):

        try:
            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t   TABLE BOOKING")
                print("\t" + "‗" * 50)

                print("\n\t\t 1  ->   Book Table")
                print("\t\t 2  ->   View Available Tables")
                print("\t\t 3  ->   Booking Status")
                print("\t\t 4  ->   Back")

                print("\t" + "‗" * 50)

                option = input("\t select any option in given menu : ")

                if option == "1":
                    self.book_table()

                elif option == "2":
                    self.view_available_tables()

                elif option == "3":
                    self.booking_status_menu()

                elif option == "4":
                    break

                else:
                    print("\t Invalid option...!")

        except Exception as error:
            logger.error(
                f"Error while in booking menu : {error}"
            )
            print(f"Unable to select any option...!")

    
    def booking_status_menu(self):

        while True:

            print("\n\t" + "‗" * 50)
            print("\n\t\t    BOOKING STATUS")
            print("\t" + "‗" * 50)

            print("\n\t\t 1  ->   View Booking By ID")
            print("\t\t 2  ->   View All Booking Status")
            print("\t\t 3  ->   Back")

            print("\t" + "‗" * 50)

            option = input(
                "\t select any option in given menu : "
            )

            if option == "1":
                self.view_booking_by_id()

            elif option == "2":
                self.view_all_booking_status()

            elif option == "3":
                break
            else:
                print("\t Invalid option ...!")

    def view_booking_by_id(self):
        while True:
            booking_id = input("Enter booking id : ")
            if table_validation.validate_id(booking_id):
                booking_id = int(booking_id)
                break
            else: 
                print("Invalid booking id...!")

        data = file_handling.read_data("database/bookings.json")
        for booking in data:
            if booking["booking_id"] == booking_id:

                print("‗" * 50)
                print(f"\n       BOOK TABLE")
                print("‗" * 50)
                print(f"Booking ID    : {booking["booking_id"]}")
                print(f"Customer Name : {booking["customer_name"]}")
                print(f"Table IDs     : {booking["table_ids"]}")
                print(f"Booking Start : {booking["booking_start"]}")
                print(f"Duration      : {booking["booking_duration"]}")
                print(f"Status        : {booking["status"]}")
                print("‗" * 50)
                
                return
        print("Id not available...!")

    def view_all_booking_status(self):

        data = file_handling.read_data("database/bookings.json")
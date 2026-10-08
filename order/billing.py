from utils import billing_utils
from utils import order_utils
from utils import file_handling
from utils import menu_utils
from validation import table_validation
from utils.time_utils import TimeManager
from utils.logger import logger

class Billing:

    def __init__(self):
        pass

    def generate_bill(self):

        try:

            while True:

                table_id = input("\t Enter table id : ")

                if table_validation.validate_id(table_id):
                    table_id = int(table_id)
                    logger.info(
                        f"Valid table id entered: {table_id}"
                    )
                    break
                else:
                    logger.warning(
                        f"Invalid table id entered: {table_id}"
                    )
                    print("\t Invalid table id...!")

            orders = order_utils.get_orders_by_table(table_id)

            if not orders:
                logger.warning(
                    f"No orders found for table id: {table_id}"
                )
                print("\t please order first...!")
                return
            logger.info(
                f"{len(orders)} order(s) found for table id: {table_id}"
            )

            valid_orders = []
            bill_items = []

            for order in orders:
                if order["status"] != "Cancelled":
                    valid_orders.append(order)
                else:
                    logger.warning(
                        f"Cancelled order skipped: "
                        f"{order['order_id']}"
                    )

            if not valid_orders:
                logger.warning(
                    f"No valid orders available for table id: {table_id}"
                )
                print("\t No valid orders available for billing...!")
                return

            for order in valid_orders:

                for item in order["items"]:
                    bill_items.append(item)

            subtotal = billing_utils.calculate_subtotal(bill_items)

            tax = billing_utils.calculate_tax(subtotal)

            discount = billing_utils.calculate_discount(subtotal)

            final_amount = billing_utils.calculate_final_amount(
                subtotal,
                tax,
                discount
            )

            bill_id = billing_utils.get_next_bill_id()

            time_manager = TimeManager()

            bill_time = time_manager.get_current_time().strftime("%Y-%m-%d %H:%M:%S")
            order_ids = []

            for order in valid_orders:
                order_ids.append(order["order_id"])

            bill_items_with_price = []
            for item in bill_items:

                menu_item = menu_utils.find_item_by_id(item["item_id"])

                if menu_item:
                    bill_items_with_price.append({
                        "item_id": item["item_id"],
                        "quantity": item["quantity"],
                        "price": menu_item["price"]
                    })
                else:
                    logger.warning(
                        f"Menu item not found: {item['item_id']}"
                    )


            bill_data = {
                "bill_id": bill_id,
                "table_id": table_id,
                "order_ids": order_ids,
                "items": bill_items_with_price,
                "subtotal": subtotal,
                "tax": tax,
                "discount": discount,
                "final_amount": final_amount,
                "bill_time": bill_time
            }

            data = file_handling.read_data("database/bills.json")

            data.append(bill_data)

            file_handling.write_data("database/bills.json", data)

            logger.info(
                f"Bill generated successfully. "
                f"Bill ID: {bill_id}, Table ID: {table_id}"
            )

            print(
                f"\n\t Bill generated successfully. "
                f"\t Bill ID: {bill_id}"
            )
            data = order_utils.get_orders()

            for order in data:

                if order["order_id"] in order_ids:
                    order["status"] = "Completed"

            file_handling.write_data("database/orders.json",data)

        except Exception as error:
            logger.error(f"Error while in generate bill : {error}")
            print("Unable generate bill...!")
        

    def get_bill(self):

        try:
            while True:
                bill_id = input("\t Enter bill id : ")
                if table_validation.validate_id(bill_id):
                    bill_id = int(bill_id)
                    logger.info(f"Valid bill id entered: {bill_id}")
                    break
                else:
                    logger.warning(f"Invalid bill id entered: {bill_id}")
                    print("Invalid bill id...!")

            bill = billing_utils.found_bill(bill_id)

            if bill is None:
                logger.warning(f"Bill not found for bill id: {bill_id}")
                print("Bill not found...!")
                return None
            
            return bill
        except Exception as error:

            logger.error(f"Unexpected error while getting bill: {error}")
            print("Unable to get bill...!")

    def view_bill(self):

        try:

            bill = self.get_bill()

            if bill is None:
                return

            print("\n" + "‗" * 50)
            print("\t\t      BILL")
            print("‗" * 50)

            print(f"\nBill ID       : {bill['bill_id']}")
            print(f"Table ID      : {bill['table_id']}")
            print(f"Order IDs     : {bill['order_ids']}")
            print(f"Bill Time     : {bill['bill_time']}")

            print("\n" + "—" * 50)
            print("\t\tItems")
            print("—" * 50)

            print(f"{'Item ID':<12}{'Quantity':<12}{'Price':<12}{'Amount':<12}")

            print("—" * 50)

            for item in bill["items"]:

                amount = item["quantity"] * item["price"]

                print(
                    f"{item['item_id']:<12}"
                    f"{item['quantity']:<12}"
                    f"{item['price']:<12}"
                    f"{amount:<12}"
                )

            print("—" * 50)

            print(f"\nSubtotal      : ₹{bill['subtotal']:.2f}")
            print(f"Tax           : ₹{bill['tax']:.2f}")
            print(f"Discount      : ₹{bill['discount']:.2f}")

            print("—" * 50)
            logger.info(f"Bill displayed successfully: {bill['bill_id']}")

            print(f"Final Amount  : ₹{bill['final_amount']:.2f}")

            print("‗" * 50)
        except Exception as error:
            logger.error(f"Unexpected error while viewing bill: {error}")
            print("\tUnable to view bill...!")


    def billing_menu(self):

        try:

            while True:

                print("\n\t" + "‗" * 50)
                print("\n\t\t      Billing Management")
                print("\t" + "‗" * 50)

                print("\n\t\t1 → Generate Bill")
                print("\t\t2 → View Bill")
                print("\t\t3 → Back")
                print("\t" + "‗" * 50)

                choice = input("\n\t\tEnter your choice : ")

                if choice == "1":
                    self.generate_bill()

                elif choice == "2":
                    self.view_bill()

                elif choice == "3":
                    break

                else:
                    print("\n\t\tInvalid choice. Please try again.")

        except Exception as error:
            logger.error(f"Error while in billing menu : {error}")
            print("\tUnable to view billing menu...!")
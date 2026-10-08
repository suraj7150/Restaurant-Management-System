from validation import order_validation
from validation import table_validation
from validation import item_validation
from utils import order_utils
from utils import file_handling
from utils.time_utils import TimeManager
from utils import table_utils
from utils import menu_utils
from order.order_item import OrderItem
from menu.menu_manager import MenuManager
from utils.logger import logger


class Order:

    def __init__(self):

        self.order_id = None
        self.table_id = None
        self.order_time = None
        self.items = []
        self.status = None

    def take_order(self):

        try:

            while True:

                self.table_id = input("\t Enter Table ID: ")

                if table_validation.validate_id(self.table_id):
                    self.table_id = int(self.table_id)
                    logger.info(f"Valid table ID entered: {self.table_id}")
                    break

                logger.warning(f"Invalid table ID entered: {self.table_id}")
                print("\t Invalid Table ID")

            table = table_utils.find_table_by_id(self.table_id)

            if table is None:
                logger.warning(f"Table not found: {self.table_id}")
                print("\t Table not found.")
                return

            booking = table_utils.get_active_booking_by_table(self.table_id)

            if booking is None:
                logger.warning(
                    f"No active booking found for table: "
                    f"{self.table_id}"
                )
                print("\t No active booking found for this table.")
                return

            MenuManager().show_item()

            while True:

                item_id = input("\t Enter Item ID: ")

                if not item_validation.validate_id(item_id):
                    logger.warning(f"Invalid item ID entered: {item_id}")
                    print("\t Invalid Item ID")
                    continue

                item_id = int(item_id)

                item = menu_utils.find_item_by_id(item_id)

                if item is None:
                    logger.warning(f"Item not found: {item_id}")
                    print("\t Item not found.")
                    continue

                if not item["isAvailable"]:
                    logger.warning(f"Unavailable item selected: {item_id}")
                    print("\t This item is currently unavailable.")
                    continue

                quantity = input("\t Enter Quantity: ")

                if not order_validation.validate_quantity(quantity):
                    logger.warning(
                        f"Invalid quantity entered for "
                        f"item {item_id}: {quantity}"
                    )
                    print("\t Invalid Quantity")
                    continue

                quantity = int(quantity)

                order_item = OrderItem(
                    item_id,
                    quantity
                )

                item_data = order_item.order_item_object()

                self.items.append(item_data)


                while True:
                    choice = input("\t Add another item? (y/n): ")
                    if choice.lower() == "y":
                        logger.info("User chose to add another item")
                        break
                    elif choice.lower() == "n":
                        logger.info("User finished adding items")
                        break
                    else:
                        logger.warning(f"Invalid add-another choice: {choice}")
                        print("\t Invalid value...!")

                if choice == "n":
                    break

            self.order_id = order_utils.get_next_order_id()

            time_manager = TimeManager()

            self.order_time = time_manager.get_current_time().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            self.status = "Pending"

            order_data = {
                "order_id": self.order_id,
                "table_id": self.table_id,
                "order_time": self.order_time,
                "items": self.items,
                "status": self.status
            }

            data = order_utils.get_orders()

            data.append(order_data)

            file_handling.write_data("database/orders.json",data)

            logger.info(
                f"Order placed successfully. "
                f"Order ID: {self.order_id}, "
                f"Table ID: {self.table_id}"
            )

            print(f"\n\t Order placed successfully.")
            print(f"\t Order ID: {self.order_id}")

        except Exception as error:
            logger.error(f"Unexpected error while taking order: {error}")
            print("\t Unable to place order...!")

    def update_order(self):
            
        try:

            order_id = input("\t Enter Order ID: ")

            if not order_validation.validate_order_id(order_id):
                logger.warning(f"Invalid order ID entered: {order_id}")
                print("\t Invalid Order ID")
                return

            order_id = int(order_id)

            order = order_utils.find_order_by_id(order_id)

            if order is None:
                logger.warning(f"Order not found: {order_id}")
                print("\t Order not found.")
                return

            if order["status"] != "Pending":
                logger.warning(
                    f"Attempt to update non-pending order: "
                    f"{order_id}, Status: {order['status']}"
                )
                print("\t Only pending orders can be updated.")
                return

            print("‗" * 40)
            print("\n\t Current Order Items")
            print("‗" * 40)

            for item in order["items"]:

                print(
                    f"\t Item ID: {item['item_id']} | "
                    f"\t Quantity: {item['quantity']}"
                )
            print("‗" * 40)
            while True:
                print("\n\t 1 → Add Item")
                print("\t 2 → Update Quantity")
                print("\t 3 → Remove Item")
                print("\t 4 → Back")

                choice = input("\t Enter your choice: ")

                if choice == "1":
                    logger.info(
                        f"User selected Add Item for order: "
                        f"{order_id}"
                    )
                    item_id = input("\t Enter Item ID: ")

                    if not item_validation.validate_id(item_id):
                        logger.warning(
                            f"Invalid item ID while updating "
                            f"order {order_id}: {item_id}"
                        )
                        print("\t Invalid Item ID")
                        continue

                    item_id = int(item_id)

                    item = menu_utils.find_item_by_id(item_id)

                    if item is None:
                        logger.warning(
                            f"Item not found while updating "
                            f"order {order_id}: {item_id}"
                        )
                        print("\t Item not found.")
                        continue

                    if not item["isAvailable"]:
                        logger.warning(
                            f"Unavailable item selected for "
                            f"order {order_id}: {item_id}"
                        )
                        print("\t This item is currently unavailable.")
                        continue

                    quantity = input("\t Enter Quantity: ")

                    if not order_validation.validate_quantity(quantity):
                        logger.warning(
                            f"Invalid quantity for item "
                            f"{item_id} in order {order_id}: "
                            f"{quantity}"
                        )
                        print("\t Invalid Quantity")
                        continue

                    quantity = int(quantity)

                    order_item = OrderItem(
                        item_id,
                        quantity
                    )

                    item_data = order_item.order_item_object()

                    order["items"].append(item_data)

                    data = order_utils.get_orders()

                    for saved_order in data:

                        if saved_order["order_id"] == order_id:
                            saved_order["items"] = order["items"]
                            break

                    file_handling.write_data(
                        "database/orders.json",
                        data
                    )
                    logger.info(
                        f"Item added successfully. "
                        f"Order ID: {order_id}, "
                        f"Item ID: {item_id}, "
                        f"Quantity: {quantity}"
                    )
                    print("\t Item added successfully.")

                elif choice == "2":
                    logger.info(
                        f"User selected Update Quantity "
                        f"for order: {order_id}"
                    )
                    item_id = input("\t Enter Item ID: ")

                    if not item_validation.validate_id(item_id):
                        logger.warning(
                            f"Invalid item ID while updating "
                            f"quantity in order {order_id}: "
                            f"{item_id}"
                        )
                        print("\t Invalid Item ID")
                        continue

                    item_id = int(item_id)

                    item_found = False

                    for item in order["items"]:

                        if item["item_id"] == item_id:

                            quantity = input("\t Enter New Quantity: ")

                            if not order_validation.validate_quantity(quantity):
                                logger.warning(
                                    f"Invalid new quantity for "
                                    f"item {item_id}, "
                                    f"order {order_id}: {quantity}"
                                )
                                print("\t Invalid Quantity")
                                break

                            quantity = int(quantity)

                            item["quantity"] = quantity

                            item_found = True
                            break

                    if not item_found:
                        logger.warning(
                            f"Item {item_id} not found in "
                            f"order {order_id}"
                        )

                        print("\t Item not found in this order.")
                        continue

                    data = order_utils.get_orders()

                    for saved_order in data:

                        if saved_order["order_id"] == order_id:
                            saved_order["items"] = order["items"]
                            break

                    file_handling.write_data(
                        "database/orders.json",
                        data
                    )

                    logger.info(
                        f"Quantity updated successfully. "
                        f"Order ID: {order_id}, "
                        f"Item ID: {item_id}, "
                        f"New Quantity: {quantity}"
                    )
                    print("\t Quantity updated successfully.")

                elif choice == "3":
                    logger.info(
                        f"User selected Remove Item "
                        f"for order: {order_id}"
                    )

                    if len(order["items"]) == 1:
                        logger.warning(
                            f"Attempt to remove last item from "
                            f"order: {order_id}"
                        )
                        print("\t Order must contain at least one item.")
                        continue

                    item_id = input("\t Enter Item ID: ")

                    if not item_validation.validate_id(item_id):
                        logger.warning(
                            f"Invalid item ID while removing "
                            f"from order {order_id}: {item_id}"
                        )
                        print("\t Invalid Item ID")
                        continue

                    item_id = int(item_id)

                    item_found = False

                    for item in order["items"]:

                        if item["item_id"] == item_id:

                            order["items"].remove(item)

                            item_found = True
                            break

                    if not item_found:
                        logger.warning(
                            f"Item {item_id} not found in "
                            f"order {order_id}"
                        )
                        print("\t Item not found in this order.")
                        continue

                    data = order_utils.get_orders()

                    for saved_order in data:

                        if saved_order["order_id"] == order_id:
                            saved_order["items"] = order["items"]
                            break

                    file_handling.write_data(
                        "database/orders.json",
                        data
                    )
                    logger.info(
                        f"Item removed successfully. "
                        f"Order ID: {order_id}, "
                        f"Item ID: {item_id}"
                    )
                    print("\t Item removed successfully.")

                elif choice == "4":
                    logger.info(
                        f"Update order process completed: "
                        f"{order_id}"
                    )
                    break

                else:
                    logger.warning(
                        f"Invalid update order choice: {choice}"
                    )
                    print("\t Invalid choice...!")

        except Exception as error:
            logger.error(f"Unexpected error while updating order: {error}")
            print("\t Unable to update order...!")


    def cancel_order(self):

        try:

            order_id = input("\t Enter Order ID: ")

            if not order_validation.validate_order_id(order_id):
                print("\t Invalid Order ID")
                return

            order_id = int(order_id)

            order = order_utils.find_order_by_id(order_id)

            if order is None:
                print("\t Order not found.")
                return

            if order["status"] != "Pending":
                print("\t Only pending orders can be cancelled.")
                return

            order["status"] = "Cancelled"

            data = order_utils.get_orders()

            for saved_order in data:

                if saved_order["order_id"] == order_id:
                    saved_order["status"] = "Cancelled"
                    break

            file_handling.write_data(
                "database/orders.json",
                data
            )

            print("\t Order cancelled successfully.")
        except Exception as error:
            logger.error(f"Unexpected error while cancelling order: {error}")
            print("\t Unable to cancel order...!")



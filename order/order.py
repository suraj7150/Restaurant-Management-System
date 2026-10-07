from validation import order_validation
from validation import table_validation
from validation import item_validation
from utils import order_utils
from utils import file_handling
from utils.time_utils import TimeManager
from utils import table_utils
from utils import menu_utils
from order.order_item import OrderItem


class Order:

    def __init__(self):

        self.order_id = None
        self.table_id = None
        self.order_time = None
        self.items = []
        self.status = None

    def take_order(self):

        while True:

            self.table_id = input("Enter Table ID: ")

            if table_validation.validate_id(self.table_id):
                self.table_id = int(self.table_id)
                break

            print("Invalid Table ID")

        table = table_utils.find_table_by_id(self.table_id)

        if table is None:
            print("Table not found.")
            return

        booking = table_utils.get_active_booking_by_table(
            self.table_id
        )

        if booking is None:
            print("No active booking found for this table.")
            return

        while True:

            item_id = input("Enter Item ID: ")

            if not item_validation.validate_id(item_id):
                print("Invalid Item ID")
                continue

            item_id = int(item_id)

            item = menu_utils.find_item_by_id(item_id)

            if item is None:
                print("Item not found.")
                continue

            if not item["isAvailable"]:
                print("This item is currently unavailable.")
                continue

            quantity = input("Enter Quantity: ")

            if not order_validation.validate_quantity(quantity):
                print("Invalid Quantity")
                continue

            quantity = int(quantity)

            order_item = OrderItem(
                item_id,
                quantity
            )

            item_data = order_item.order_item_object()

            self.items.append(item_data)

            choice = input("Add another item? (y/n): ")

            if choice.lower() == "n":
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

        file_handling.write_data(
            "database/orders.json",
            data
        )

        print(f"\nOrder placed successfully. Order ID: {self.order_id}")

    def update_order(self):

        order_id = input("Enter Order ID: ")

        if not order_validation.validate_order_id(order_id):
            print("Invalid Order ID")
            return

        order_id = int(order_id)

        order = order_utils.find_order_by_id(order_id)

        if order is None:
            print("Order not found.")
            return

        if order["status"] != "Pending":
            print("Only pending orders can be updated.")
            return

        print("\nCurrent Order Items")
        print("-" * 40)

        for item in order["items"]:

            print(
                f"Item ID: {item['item_id']} | "
                f"Quantity: {item['quantity']}"
            )

        while True:
            print("\n1 → Add Item")
            print("2 → Update Quantity")
            print("3 → Remove Item")
            print("4 → Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                
                item_id = input("Enter Item ID: ")

                if not item_validation.validate_id(item_id):
                    print("Invalid Item ID")
                    continue

                item_id = int(item_id)

                item = menu_utils.find_item_by_id(item_id)

                if item is None:
                    print("Item not found.")
                    continue

                if not item["isAvailable"]:
                    print("This item is currently unavailable.")
                    continue

                quantity = input("Enter Quantity: ")

                if not order_validation.validate_quantity(quantity):
                    print("Invalid Quantity")
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

                print("Item added successfully.")

            elif choice == "2":

                item_id = input("Enter Item ID: ")

                if not item_validation.validate_id(item_id):
                    print("Invalid Item ID")
                    continue

                item_id = int(item_id)

                item_found = False

                for item in order["items"]:

                    if item["item_id"] == item_id:

                        quantity = input("Enter New Quantity: ")

                        if not order_validation.validate_quantity(quantity):
                            print("Invalid Quantity")
                            break

                        quantity = int(quantity)

                        item["quantity"] = quantity

                        item_found = True
                        break

                if not item_found:
                    print("Item not found in this order.")
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

                print("Quantity updated successfully.")

            elif choice == "3":

                if len(order["items"]) == 1:
                    print("Order must contain at least one item.")
                    continue

                item_id = input("Enter Item ID: ")

                if not item_validation.validate_id(item_id):
                    print("Invalid Item ID")
                    continue

                item_id = int(item_id)

                item_found = False

                for item in order["items"]:

                    if item["item_id"] == item_id:

                        order["items"].remove(item)

                        item_found = True
                        break

                if not item_found:
                    print("Item not found in this order.")
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

                print("Item removed successfully.")

            elif choice == "4":
                break

            else:
                print("Invalid choice")

    def cancel_order(self):

        order_id = input("Enter Order ID: ")

        if not order_validation.validate_order_id(order_id):
            print("Invalid Order ID")
            return

        order_id = int(order_id)

        order = order_utils.find_order_by_id(order_id)

        if order is None:
            print("Order not found.")
            return

        if order["status"] != "Pending":
            print("Only pending orders can be cancelled.")
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

        print("Order cancelled successfully.")
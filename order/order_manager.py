from order.order import Order


class OrderManager:

    def __init__(self):
        self.order = Order()

    def order_menu(self):

        while True:

            print("\n\t" + "‗" * 50)
            print("\n\t\t      Order Management")
            print("\t" + "‗" * 50)

            print("\n\t\t1 → Take Order")
            print("\t\t2 → Update Order")
            print("\t\t3 → Cancel Order")
            print("\t\t4 → Back")
            
            print("\t" + "‗" * 50)

            choice = input("\n\t\tEnter your choice: ")

            if choice == "1":
                self.order.take_order()

            elif choice == "2":
                self.order.update_order()

            elif choice == "3":
                self.order.cancel_order()

            elif choice == "4":
                break

            else:
                print("\n\t\tInvalid choice. Please try again.")
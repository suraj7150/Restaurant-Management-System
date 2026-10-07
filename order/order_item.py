
class OrderItem:

    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity

    def order_item_object(self):
        return {
            "item_id": self.item_id,
            "quantity":self.quantity
        }

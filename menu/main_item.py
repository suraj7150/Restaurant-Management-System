import json

class MenuItem:

    def __init__(self, item_id, name, category, price, is_veg, is_available):
        self.item = {
            "id" : item_id ,
            "name" : name ,
            "category" : category ,
            "price" : price ,
            "isVeg" : is_veg ,
            "isAvailable" : is_available ,
        }
    

    def item_object(self):
        return self.item

    
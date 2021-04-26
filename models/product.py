class Product:

    def __init__(self, name, description, quantity, buying_cost, selling_price, manufacturer_id, id= None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer_id = manufacturer_id
        self.id = id
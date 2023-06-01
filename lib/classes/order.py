
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) == int and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Not a valid price")
        
    # @property
    # def 

class Coffee:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not (hasattr(self, 'name')) and type(name) == str:
            self._name = name      
        else:
            raise Exception("Cannot change coffee name")
        
    def orders(self):
        # for each order in the list of all orders, return coffee that matches this coffee(example vanilla latte)
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        # return  [order.customer for order in Order.all if order.coffee == self]
        # return [order.customer for order in self.orders()] #shorter version of line above
        # this is unique because of set -> curly braces
        return list({order.customer for order in Order.all if order.coffee == self}) 
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        all_prices = [order.price for order in self.orders()]
        if all_prices:
            return sum(all_prices) / len(all_prices)

from classes.customer import Customer
from classes.order import Order
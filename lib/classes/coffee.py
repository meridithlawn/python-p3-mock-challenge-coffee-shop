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
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

from classes.customer import Customer
from classes.order import Order
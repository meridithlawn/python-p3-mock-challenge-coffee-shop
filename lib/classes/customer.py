class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception("Names must be a string between 1 and 15 characters")
        
    def orders(self):
        pass
    
    def coffees(self):
        from classes.coffee import Coffee
        pass
from classes.order import Order
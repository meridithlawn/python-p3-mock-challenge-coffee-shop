
class Order:

    all =[]

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        # below: type of this one individual order type(self) is like saying Order.all
        # will be called from Order.__init__ is the step in line below
        type(self).all.append(self)
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if type(price) == int and 1 <= price <= 10:
            self._price = price
        else:
            raise Exception("Not a valid price")
        
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        # if isinstance(customer, Customer):
        if type(customer) == Customer:
            self._customer = customer
            # return self._customer
        else:
            raise Exception("not of type Customer")
        
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        if type(coffee) == Coffee:
            self._coffee = coffee
            # return self._coffee # if you type Order.coffee then it should return a coffee of the Coffee Class
        else:
            raise Exception("not of type Coffee")


from classes.customer import Customer
from classes.coffee import Coffee



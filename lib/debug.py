#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

    latte = Coffee("latte")
    black = Coffee("black")
    jess = Customer("Jess")
    drew = Customer("Drew")
    meridith = Customer("meridith")
    order_1 = Order(jess, black, 3)
    order_2 = Order(drew, latte, 5)
    order_3 = Order(jess, black, 3)

    ipdb.set_trace()

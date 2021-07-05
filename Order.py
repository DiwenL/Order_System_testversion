import datetime
import os, sys


class Order:
    
    def __init__(self,orderName, price, amount = 1,comment = ''):
        self.name = orderName
        self.amount = amount
        self.price = price
        self.comments = []
        self.totalCost = price * amount
        if comment != '':
            self.comments.append(comment)
        return

        
    def set_amount(self, amount):
        self.amount = amount
        self.totalCost = self.price * self.amount
        return

    def set_price(self,price):
        self.price = price
        return

    def set_type(self,t):
        self.orderType = t
        return

    def add_comment(self,c):
        self.comments.append(c)
        return
    
    def set_total_cost(self,tcost):
        self.totalCost = tcost
        return

    
    def show_order(self):
        info =  self.name + " x" + str(self.amount) 
        if len(self.comments) != 0:
            for comment in self.comments:
                info += "\n --"
                info += comment
        info += "\n                           $" + str(self.totalCost)
        return info

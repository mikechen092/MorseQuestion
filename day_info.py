import datetime


class Day_Info():

    #initialize the date_price class with a datetime object and a price
    def __init__(self,dt_obj,p,q):

        self.date_time = dt_obj

        self.price = p

        self.quantity = q

    def get_price(self):

        return self.price

    # returns quantity
    def get_quantity(self):

        return self.quantity

    # returns the datetime obj
    def get_date(self):

        return self.date_time

    # returns true/false when comparing to another date_price obj (NECESSARY?)
    # def compare(self,other_dt):


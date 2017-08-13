import datetime


class Day_Info():

    #initialize the date_price class with a datetime object and a price
    def __init__(self,dt_obj,p,q):

        self.date_time = dt_obj

        self.price = p

        self.quantity = q

    # returns price
    def get_price(self):

        return self.price

    # returns quantity
    def get_quantity(self):

        return self.quantity

    # returns the datetime obj
    def get_date(self):

        return self.date_time

    # given another day_info object check if the two are equivalent
    def compare(self,other_di_obj):

        if (self.date_time == other_di_obj.get_date() and
        self.price == other_di_obj.get_price() and
        self.quantity == other_di_obj.get_quantity()):
            return True

        return False



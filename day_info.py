import datetime


class Day_Info():

    #initialize the date_price class with a datetime object and a price
    def __init__(self,dt_obj,p,u):

        self.date_time = dt_obj

        self.price = p

        self.units = u

    # returns price
    def get_price(self):

        return self.price

    # returns number of units
    def get_units(self):

        return self.units

    # returns the datetime obj
    def get_date(self):

        return self.date_time

    # given another day_info object check if the two are equivalent
    def compare(self,other_di_obj):

        if (self.date_time == other_di_obj.get_date() and
        self.price == other_di_obj.get_price() and
        self.units == other_di_obj.get_units()):
            return True

        return False



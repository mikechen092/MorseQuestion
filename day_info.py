import datetime


class Day_Info():

    # initialize a Day_info object with a datetime, price, and units
    def __init__(self,dt_obj,p,u):

        self.date_time = dt_obj

        self.price = p

        self.units = u

    # get_price - returns price
    def get_price(self):

        return self.price

    # get_units - returns number of units
    def get_units(self):

        return self.units

    # get_date - returns the datetime obj
    def get_date(self):

        return self.date_time

    # compare - returns True or False if the other Day_info object has the
    #           same values as the current
    #   @param other_di_object - another Day_info object to compare to
    def compare(self,other_di_obj):

        if (self.date_time == other_di_obj.get_date() and
        self.price == other_di_obj.get_price() and
        self.units == other_di_obj.get_units()):
            return True

        return False



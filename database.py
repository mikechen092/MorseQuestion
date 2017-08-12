import day_info
import datetime

class Database():

    def __init__(self):

        # array of sorted date_price obj by date

        self.db = []

        # TODO: check if want to use hashtable instead of array? ->
        # look up constant & searching for two for average nlogn + change
        # vs.
        # binary search for item & not found then you know where to average nlogn

    # takes in a new day_info -> uses insertion sort
    # TODO: DUPLICATES????
    def add_entry(self,di_obj):

        entry_num = 0
        while(entry_num < len(self.db)):

            if di_obj.get_date() < self.db[entry_num].get_date():

                break

            entry_num += 1

        self.db.insert(entry_num,di_obj)

    # gets min time in db -> assumes caller knows db is filled
    def get_min(self):

        return self.db[0]

    # gets max time in db -> assumes caller knows db is filled
    def get_max(self):

        return self.db[-1]

    # looks up a value by the datetime object returns day info obj
    def lookup(self,dt_obj):

        # if the datetime obj is less than the smallest entry in the db then return the price of the smallest in the db
        if dt_obj < self.db[0].get_date():
            return self.db[0].get_price()

        # if the datetime obj is greater than the largest entry in the db then return the price of the largest in the db
        elif dt_obj > self.db[-1].get_date():
            return self.db[-1].get_price()

        # try to find the date in the db, if not return the average of the adjacent entries
        for i in range(len(self.db)):

            if dt_obj == self.db[i].get_date():

                return self.db[i].get_price()

            elif dt_obj < self.db[i].get_date():
                # can put + 1 without worrying about bounds b/c checks above
                return (self.db[i].get_price() + self.db[i - 1].get_price())/2

    # looks up all values within the two datetime obj returns array of day_info obj
    #TODO: need to implement
    def lookup_range(self,dt_obj1,dt_obj2):
        print('this is going to be an array')

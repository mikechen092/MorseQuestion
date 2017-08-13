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
    # if the datetime is not in the database then you get the two adjacent
    # if the datetime is int he database you get two of the same object
    def lookup(self,dt_obj):

        # if the datetime obj is less than the smallest entry in the db then return the smallest di_obj
        if dt_obj < self.db[0].get_date():
            return (self.db[0],self.db[0])

        # if the datetime obj is greater than the largest entry in the db then return the largest di_obj
        elif dt_obj > self.db[-1].get_date():
            return (self.db[-1],self.db[-1])

        # try to find the date in the db, if not return the average of the adjacent entries
        for i in range(len(self.db)):

            if dt_obj == self.db[i].get_date():

                return (self.db[i],self.db[i])

            elif dt_obj < self.db[i].get_date():
                # can put + 1 without worrying about bounds b/c checks above
                return (self.db[i-1],self.db[i])

    # looks up all values within the two datetime obj returns array of day_info obj
    def lookup_range(self,dt_obj1,dt_obj2):

        # initialize base case if the two datetimes are less than the smallest and larger than the largest in the db
        low_index = 0
        high_index = len(self.db)

        # find the first index where the smaller datetime is less than equal to something in the database
        for i in range(len(self.db)):

            if dt_obj1 <= self.db[i].get_date():
                low_index = i
                break

        # find the first index where the larger datetime is greater than equal to something in the db
        for i in range(len(self.db)-1,-1,-1):

            if dt_obj2 >= self.db[i].get_date():
                # add one to the index b/c last number is non-inclusive
                high_index = i + 1
                break

        # take part of the database and return the array
        arr = self.db[low_index:high_index]

        return arr

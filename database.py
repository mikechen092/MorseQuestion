import day_info
import datetime

class Database():

    # initialize Database class with an array to store the di_objects in
    def __init__(self):

        # array of sorted date_price obj by date
        self.db = []


    #add_entry - takes in a new day_info and inserts it in the correct place
    #    @param di_obj - the Day_info object to be added to the array
    def add_entry(self,di_obj):

        entry_num = 0
        while(entry_num < len(self.db)):

            # if there is a duplicate then print a warning and do not add the value to the database
            if di_obj.compare(self.db[entry_num]):

                print("Warning: Attempted to add duplicate entry with date",str(di_obj.get_date()))
                return

            if di_obj.get_date() < self.db[entry_num].get_date():

                break

            entry_num += 1

        self.db.insert(entry_num,di_obj)

    # is_empty - returns True if empty and False is not empty
    def is_empty(self):

        if len(self.db) == 0:
            return True

        return False

    # get_min - returns the smallest datetime in the db array
    #   assumes caller knows db is not empty
    def get_min(self):

        return self.db[0]

    # get_min - returns the largest datetime in the db array
    #   assumes caller knows db is not empty
    def get_max(self):

        return self.db[-1]

    # lookup - returns a tuple of either two of the same Day_Info object if the
    #          datetime is in the array. returns a tuple of adjacent Day_info objects
    #          if the datetime is not in the array
    #   @param dt_obj - datetime to lookup
    #   @return a tuple of two Day_Info objects
    def lookup(self,dt_obj):

        # if the datetime obj is less than the smallest entry in the db then return the smallest di_obj
        if dt_obj < self.db[0].get_date():
            return (self.db[0],self.db[0])

        # if the datetime obj is greater than the largest entry in the db then return the largest di_obj
        elif dt_obj > self.db[-1].get_date():
            return (self.db[-1],self.db[-1])

        # try to find the date in the db, if not return the average of the adjacent entries
        for i in range(1,len(self.db)):

            if dt_obj == self.db[i].get_date():

                return (self.db[i],self.db[i])

            elif dt_obj < self.db[i].get_date():

                return (self.db[i-1],self.db[i])

    # lookup_range - returns an array of Day_Info objects with datetimes that fall within
    #                the range given by two datetime
    #   @param dt_obj1 - datetime defining the lower end of the range to search
    #   @param dt_obj2 - datetime defining the upper end of the range to search
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

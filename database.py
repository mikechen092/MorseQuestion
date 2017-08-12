

class Database():

    def __init__(self,filename):

        # array of sorted date_price obj by date

        self.db = []

        # want to use hashtable instead of array? ->
        # look up constant & searching for two for average nlogn + change
        # vs.
        # binary search for item & not found then you know where to average nlogn

    # takes in a new day_info object and places it in the correct spot in db

    def add_entry(self,di_obj):

        return

    # looks up a value by the datetime object

    def lookup(self,dt_obj):

        return

    # TODO: add more functions (?)
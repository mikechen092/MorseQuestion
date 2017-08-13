import datetime
from pytz import timezone
import dateutil.parser
import argparse
from math import sqrt
from day_info import Day_Info
from database import Database

"""
ERROR CODES
1.FileNotFound in parse_file
2.ValueError for datetime in parse_file
3.ValueError for price in parse_file
4.ValueError for unit in parse_file
5.EmptyDbError in search_db
6.TypeError for given date_time in search_db
7.EmptyDbError in get_statistics
8.NumberOfArgumentsError in main


"""
#TODO: find a way to check print statements in unittest

# get_statistics returns statistics about a range of values within the database defined by CLI given datetime objects
def get_statistics(date_time1,date_time2,db):

    # if the database is empty there cannot be any information returned
    if db.is_empty():

        print("File has no entries therefore cannot return information")
        return 7

    else:
        # need to know which is the larger date and which is the smaller date
        min_date = min(date_time1,date_time2)
        max_date = max(date_time1,date_time2)

        # convert dates into UTC to resolve compatibility issues
        min_date_utc = min_date.replace(tzinfo=timezone('UTC'))
        max_date_utc = max_date.replace(tzinfo=timezone('UTC'))

        # get the array of database entries that lie in the range defined by min_date and max_date
        date_info_arr = db.lookup_range(min_date_utc,max_date_utc)

        if len(date_info_arr) == 0:
            print("No entries in the file within the given dates. Giving information about adjacent dates.")
            val = search_db(max_date_utc,db)
            return val

        price_arr = []
        units_arr = []
        max_price = -float("inf")
        min_price = float("inf")
        avg_price = 0
        avg_units = 0
        sd_units = 0

        # search the array returned by lookup_range for the information relevant to the statistics desired
        for di in date_info_arr:

            if max_price < di.get_price():
                max_price = di.get_price()

            if min_price > di.get_price():
                min_price = di.get_price()

            # store the prices and units into separate arrays for later use
            price_arr.append(di.get_price())
            units_arr.append(di.get_units())

            avg_price += di.get_price()
            avg_units += di.get_units()

        # calculate the average price and the average units
        avg_price /= float(len(date_info_arr))
        avg_units /= float(len(date_info_arr))

        # sort the units array to find the median -> python sorts in nlogn
        units_arr.sort()

        # output price information
        print("Average Price:  %.2f" %avg_price)
        print("Minimum Price:  %.2f" %min_price)
        print("Maximum Price:  %.2f" %max_price)

        if len(date_info_arr) == 1:
            print("Median Units:  %.2f" %units_arr[0])

        else:
            # find the median of the units_arr
            if len(units_arr) % 2 == 0:

                median_units = (units_arr[int(len(units_arr)/2)] + units_arr[int(len(units_arr)/2)-1])/2
                print("Median Units:  %.2f" %median_units)

            else:

                print("Median Units:  %.2f" %units_arr[len(units_arr)/2])

        # calculate the standard deviation
        for num in units_arr:

            sd_units += abs((avg_units - num)**2)

        sd_units /= float(len(units_arr))
        sd_units = sqrt(sd_units)
        print("Standard Deviation of Units: %.2f" %sd_units)

        return 0


# search_db searches the db for the desired datetime object and prints the information
def search_db(date_time, db):

    # if the database is empty there cannot be any information returned
    if db.is_empty():

        print("File has no entries therefore cannot return information")
        return 5

    else:

        # try to compare the date given with the smallest day_info object
        try:
            print(date_time)
            # make sure date_time given is in UTC or else you cannot comapre
            date_time_utc = date_time.replace(tzinfo=timezone('UTC'))

            # if the date given is smaller than the smallest entry in the database then
            # return information about the smallest entry in the database
            if date_time_utc < db.get_min().get_date():
                print("Datetime object given is smaller than the smallest entry found in the file. "
                      "Returning information about smallest item")
                print("Price at ",str(db.get_min().get_date()),": %.2f" %(db.get_min().get_price()))

            # if the date given is larger than the largest entry in the database then
            # return information about the largest entry in the database
            elif date_time_utc > db.get_max().get_date():
                print("Datetime object given is larger than the largest entry found in the file. "
                      "Returning information about largest item")
                print("Price at ",str(db.get_max().get_date()),": %.2f" %(db.get_max().get_price()))

            else:
                # the lookup function always returns a tuple of two day_info objects
                (di_1,di_2) = db.lookup(date_time_utc)

                # if the two objects are the same then the date given is included in the database
                if di_1.compare(di_2):

                    print("Price at ",str(di_1.get_date()), ": %.2f" %(di_1.get_price()))

                # if the two objects are not the same then the date given is not included in the
                # database so you need to average the adjacent entries
                else:

                    avg = (di_1.get_price() + di_2.get_price())/2

                    print("Price at ",str(date_time_utc),": %.2f" %(avg))

            return 0

        # if there is a type error when comparing the given object and the smallest day_info date
        # then the object given is not a datetime object
        except:

            print("Object given is ",str(type(date_time))," and cannot be compared to a datetime object")
            return 6

# every line in the file is taken and converted into a day_info obj
def parse_file(filename,db):

    # if you cannot open the file then exit w/ an error message
    try:

        f = open(filename,'r')

        # information about the line number to help give more information about error messages
        linenum = 0

        for line in f:

            linenum += 1
            time, price, units = line.split(' ')

            # make sure the date in the file is in the appropriate format
            try:

                dt = dateutil.parser.parse(time)
                # make sure timezone is converted into UTC
                dt_utc = dt.replace(tzinfo=timezone('UTC'))


            except ValueError:
                print("Error in parsing. Make sure in line %d the time is in ISO-8061 format" %linenum)
                return 2

            # make sure the price in the file is in the appropriate format
            try:
                p = float(price)

            except ValueError:
                print("Error in parsing. Make sure in line %d the price is a valid value" %linenum)
                return 3

            # make sure the units in the file is in the appropriate format
            try:
                q = int(units)

            except ValueError:
                print("Error in parsing. Make sure in line %d the number of units is a valid value" %linenum)
                return 4

            # create a new day_info object and add it to the database
            new_di = Day_Info(dt_utc, float(price), int(units))
            db.add_entry(new_di)

        f.close()
        return 0

    # give user error message
    except FileNotFoundError:
        print("Could not open file path \"",filename,"\". Make sure file is in correct directory")
        return 1


# main functionality of the statistics tool parses for 2 - 3 args
# 2 args is checking to see price of specific datetime
# 3 args is pulling all datetimes within a range and printing statistics
def main():

    parser = argparse.ArgumentParser(description='Statistics Tool')
    parser.add_argument('filepath',help='file path containing datetime price and number of units')
    parser.add_argument('datetimes', metavar='D', type=str, nargs='+',help='list of datetimes')
    args = vars(parser.parse_args())
    db = Database()
    val = parse_file(args['filepath'],db)
    if val == 0:

        if len(args['datetimes']) == 1:
            # do the lookup
            return search_db(args['datetimes'][0],db)

        elif len(args['datetimes']) == 2:
            # do the statistics
            dt1 = args['datetimes'][0]
            dt2 = args['datetimes'][1]
            return get_statistics(dt1,dt2,db)
        else:
            print('Too many datetime inputs. Statistics_tool takes max of 2 datetimes, given ' + str(len(args['datetimes'])))
            return 8

    else:
        return val


if __name__ == '__main__':
    main()
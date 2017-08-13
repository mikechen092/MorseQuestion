import datetime
from pytz import timezone
import dateutil.parser
import argparse
from day_info import Day_Info
from database import Database

# TODO: test this function
# search_db searches the db for the desired datetime object and prints the information
def search_db(date_time, db):

    # if the database is empty there cannot be any information returned
    if db.is_empty():

        print("File has no entries therefore cannot return information")
        return 5

    else:

        # try to compare the date given with the smallest day_info object
        try:
            date_time_utc = date_time.replace(tzinfo=timezone('UTC'))
            # if the date given is smaller than the smallest entry in the database then
            # return information about the smallest entry in the database
            if date_time_utc < db.get_min().get_date():
                print("hello")
                print("Datetime object given is smaller than the smallest entry found in the file. "
                      "Returning information about smallest item")
                print("Price at " + str(db.get_min().get_date()) + ": " + str(db.get_min().get_price()))
                return 0

            # if the date given is larger than the largest entry in the database then
            # return information about the largest entry in the database
            elif date_time_utc > db.get_max().get_date():
                print("Datetime object given is larger than the largest entry found in the file. "
                      "Returning information about largest item")
                print("Price at " + str(db.get_max().get_date()) + ": " + str(db.get_max().get_price()))

            else:
                # the lookup function always returns a tuple of two day_info objects
                (di_1,di_2) = db.lookup(date_time_utc)

                # if the two objects are the same then the date given is included in the database
                if di_1.compare(di_2):

                    print("Price at " + str(di_1.get_date()) + ": " + str(di_1.get_price()))

                # if the two objects are not the same then the date given is not included in the
                # database so you need to average the adjacent entries
                else:

                    avg = (di_1.get_price() + di_2.get_price())/2

                    print("Price at " + str(date_time_utc) + ": " + str(avg))

            return 0
        # if there is a type error when comparing the given object and the smallest day_info date
        # then the object given is not a datetime object
        except:

            print("Object given is not datetime object")
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


            except ValueError:
                print("Error in parsing. Make sure in line " + str(linenum) +  "  the time is in ISO-8061 format")
                return 2

            # make sure the price in the file is in the appropriate format
            try:
                p = float(price)

            except ValueError:
                print("Error in parsing. Make sure in line " + str(linenum) +  " the price is a valid value")
                return 3

            # make sure the units in the file is in the appropriate format
            try:
                q = int(units)

            except ValueError:
                print("Error in parsing. Make sure in line " + str(linenum) + " the number of units is a valid value")
                return 4

            # create a new day_info object and add it to the database
            new_di = Day_Info(dt, float(price), int(units))
            db.add_entry(new_di)

        f.close()
        return 0

    # give user error message
    except FileNotFoundError:
        print("Could not open file path \"" + filename + "\". Make sure file is in correct directory")
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
            return search_db(args['datetimes'],db)

        elif len(args['datetimes']) == 2:
            # do the statistics
            print('doing statistics')
            return 8 #TODO: change value later
        else:
            print('Too many datetime inputs. Statistics_tool takes max of 2 datetimes, given ' + str(len(args['datetimes'])))
            return 7 #TODO: change value later

    else:
        return val


if __name__ == '__main__':
    main()
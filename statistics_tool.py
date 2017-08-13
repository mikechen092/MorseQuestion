import datetime
import dateutil.parser
import argparse
from day_info import Day_Info
from database import Database

def search_db(date_time, db):

    if db.is_empty():

        print("File has no entries therefore cannot return information")

    else:
        try:
            if datetime < db.get_min().get_date():
                print("Datetime object given is smaller than the smallest entry found in the file. "
                      "Returning information about smallest item")

            elif datetime > db.get_max().get_date():
                print("Datetime object given is larger than the largest entry found in the file. "
                      "Returning information about largest item")
            else:
                (di_1,di_2) = db.lookup(datetime)

                if di_1.compare(di_2):

                    print("Price at " + di_1.get_date() + ": " + int(di_1.get_price()))

                else:

                    avg = (di_1.get_price() + di_2.get_price())/2

                    print("Price at " + date_time + ": " + int(avg))


        except TypeError:

            print("Object given is not datetime object")

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
            new_di = Day_Info(time, float(price), int(units))
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

    if parse_file(args['filepath'],db) == 0:

        if len(args['datetimes']) == 1:
            # do the lookup
            search_db(args['datetimes'],db)

        elif len(args['datetimes']) == 2:
            # do the statistics
            print('doing statistics')

        else:
            print('Too many datetime inputs. Statistics_tool takes max of 2 datetimes, given ' + str(len(args['datetimes'])))
            return

    else:
        return


if __name__ == '__main__':
    main()
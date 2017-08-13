import datetime
import dateutil.parser
import argparse
from day_info import Day_Info
from database import Database

# every line in the file is taken and converted into a day_info obj
# TODO: need to test
def parse_file(filename,db):

    try:
        f = open(filename,'r')
        for line in f:
            time, price, units = line.split(' ')
            try:
                dt = dateutil.parser.parse(time)
            except:
                print("Error in parsing time. Make sure time is in ISO-8061 format")
                return -1
            new_di = Day_Info(time, price, units)
            db.add_entry(new_di)

        f.close()
        return 0
    except:
        print("Could not open file path. Make sure file is in correct directory")


# main functionality of the statistics tool parses for 2 - 3 args
# 2 args is checking to see price of specific datetime
# 3 args is pulling all datetimes within a range and printing statistics
def main():

    parser = argparse.ArgumentParser(description='Statistics Tool')
    parser.add_argument('filepath',help='file path containing datetime price and number of units')
    parser.add_argument('datetimes', metavar='D', type=str, nargs='+',
                        help='list of datetimes')
    args = vars(parser.parse_args())
    db = Database()
    if parse_file(args['filepath'],db):

        if len(args['datetimes']) == 1:
            # do the lookup
            print('doing lookup')

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
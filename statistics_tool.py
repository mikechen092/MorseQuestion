import datetime
import dateutil.parser
import argparse

def main():
    print('hello')
    parser = argparse.ArgumentParser(description='Statistics Tool')
    parser.add_argument('filepath',help='file path containing datetime price and number of units')
    parser.add_argument('datetimes', metavar='D', type=str, nargs='+',
                        help='list of datetimes')
    args = parser.parse_args()
    print(args)
    # if len(args) == 2:
    #     # do the lookup
    #     print('doing lookup')
    # elif len(args) == 3:
    #     # do the comparison
    #     print('doing comparison')
    #
    # else:
    #     print('Too many arguments. Try again')
    #     return

if __name__ == '__main__':
    main()
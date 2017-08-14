import unittest
import datetime
import sys
from io import StringIO
from statistics_tool import parse_file, search_db, get_statistics
from database import Database
from day_info import Day_Info

# testing day_info functions
class TestDI(unittest.TestCase):

    # tests if get_date returns the correct date
    def test_get_date(self):

        di = Day_Info(datetime.datetime(2005,1,2,3,4),100,2)

        self.assertEqual(datetime.datetime(2005,1,2,3,4),di.get_date())

    # tests if get_price returns the correct price
    def test_get_price(self):

        di = Day_Info(datetime.datetime(2005, 1, 2, 3, 4), 100, 2)

        self.assertEqual(100, di.get_price())

    def test_get_units(self):

        di = Day_Info(datetime.datetime(2005, 1, 2, 3, 4), 100, 2)

        self.assertEqual(2, di.get_units())

    def test_compare_same(self):

        di_1 = Day_Info(datetime.datetime(2005,1,2,3),1,2)
        di_2 = Day_Info(datetime.datetime(2005,1,2,3),1,2)

        self.assertEqual(di_1.compare(di_2),True)

    def test_compare_different_date(self):

        di_1 = Day_Info(datetime.datetime(2005, 1, 2, 4), 1, 2)
        di_2 = Day_Info(datetime.datetime(2005, 1, 2, 3), 1, 2)

        self.assertEqual(di_1.compare(di_2), False)

    def test_compare_different_price(self):

        di_1 = Day_Info(datetime.datetime(2005, 1, 2, 3), 1, 2)
        di_2 = Day_Info(datetime.datetime(2005, 1, 2, 3), 2, 2)

        self.assertEqual(di_1.compare(di_2), False)

    def test_compare_different_units(self):

        di_1 = Day_Info(datetime.datetime(2005, 1, 2, 3), 1, 2)
        di_2 = Day_Info(datetime.datetime(2005, 1, 2, 3), 1, 100)

        self.assertEqual(di_1.compare(di_2), False)

# testing database functions
class TestDB(unittest.TestCase):

    # tests if is_empty returns true when there are no entries in the database
    def test_is_empty_true(self):
        db = Database()

        self.assertTrue(db.is_empty())

    # tests if is_empty returns false if there is an entry in the database
    def test_is_empty_false(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005, 3, 1), 5, 1)

        db.add_entry(day_info1)

        self.assertFalse(db.is_empty())

    # tests to see if get min gets the smallest date in the database
    def test_get_min(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005, 3, 1), 5, 1)
        day_info2 = Day_Info(datetime.datetime(2005, 3, 2), 20, 2)
        day_info3 = Day_Info(datetime.datetime(2005, 3, 3), 50, 3)
        day_info4 = Day_Info(datetime.datetime(2005, 3, 4), 10, 4)
        day_info5 = Day_Info(datetime.datetime(2005, 3, 5), 6, 5)
        day_info6 = Day_Info(datetime.datetime(2005, 3, 6), 9, 6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        self.assertTrue(db.get_min().compare(day_info1))

    # tests to see if get max gets the largest date in the database
    def test_get_max(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005, 3, 1), 5, 1)
        day_info2 = Day_Info(datetime.datetime(2005, 3, 2), 20, 2)
        day_info3 = Day_Info(datetime.datetime(2005, 3, 3), 50, 3)
        day_info4 = Day_Info(datetime.datetime(2005, 3, 4), 10, 4)
        day_info5 = Day_Info(datetime.datetime(2005, 3, 5), 6, 5)
        day_info6 = Day_Info(datetime.datetime(2005, 3, 6), 9, 6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        self.assertTrue(db.get_max().compare(day_info6))

    # tests add_entry when the datetimes listed in the file are in ascending order
    def test_add_in_order(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        inside = db.db

        self.assertTrue(inside[0].compare(day_info1))
        self.assertTrue(inside[1].compare(day_info2))
        self.assertTrue(inside[2].compare(day_info3))
        self.assertTrue(inside[3].compare(day_info4))
        self.assertTrue(inside[4].compare(day_info5))
        self.assertTrue(inside[5].compare(day_info6))

    # tests add_entry when the datetimes listed in the file are not in order
    def test_add_out_of_order(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info2)
        db.add_entry(day_info5)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info1)
        db.add_entry(day_info6)

        inside = db.db

        self.assertTrue(inside[0].compare(day_info1))
        self.assertTrue(inside[1].compare(day_info2))
        self.assertTrue(inside[2].compare(day_info3))
        self.assertTrue(inside[3].compare(day_info4))
        self.assertTrue(inside[4].compare(day_info5))
        self.assertTrue(inside[5].compare(day_info6))

    # tests lookup to see if correct day_info object is obtained from the database if datetime is
    #  in the database
    def test_lookup_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        tup = db.lookup(datetime.datetime(2005,3,2))

        self.assertTrue(tup[0].compare(day_info2))
        self.assertTrue(tup[1].compare(day_info2))


    # tests lookup to see if correct day_info objects are obtained from the database if the datetime
    # is not in the database
    def test_lookup_not_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)
        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        tup = db.lookup(datetime.datetime(2005,3,1,5))

        self.assertTrue(tup[0].compare(day_info1))
        self.assertTrue(tup[1].compare(day_info2))

    # test lookup if the datetime is less than the smallest datetime in the database if it returns
    # the smallest day_info obj in the database
    def test_lookup_not_included_less_than(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        tup = db.lookup(datetime.datetime(2005,2,28))

        self.assertTrue(tup[0].compare(day_info1))
        self.assertTrue(tup[1].compare(day_info1))

    # tests lookup_range if the two datetimes provided are in the database
    def test_lookup_range_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        arr = db.lookup_range(datetime.datetime(2005,3,3),datetime.datetime(2005,3,5))

        self.assertEqual(len(arr),3)

        self.assertTrue(arr[0].compare(day_info3))
        self.assertTrue(arr[1].compare(day_info4))
        self.assertTrue(arr[2].compare(day_info5))

    # tests lookup_range to see if provided two datetimes outside of the range of the database
    def test_lookup_range_entire(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        arr = db.lookup_range(datetime.datetime(2005,2,28),datetime.datetime(2005,3,7))

        self.assertEqual(len(arr),6)

        self.assertTrue(arr[0].compare(day_info1))
        self.assertTrue(arr[1].compare(day_info2))
        self.assertTrue(arr[2].compare(day_info3))
        self.assertTrue(arr[3].compare(day_info4))
        self.assertTrue(arr[4].compare(day_info5))
        self.assertTrue(arr[5].compare(day_info6))

    # tests lookup_range if the two datetimes are within the range of the database, but are not included
    # in the database
    def test_lookup_range_not_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        arr = db.lookup_range(datetime.datetime(2005,3,1,5),datetime.datetime(2005,3,4,5))

        self.assertEqual(len(arr),3)

        self.assertTrue(arr[0].compare(day_info2))
        self.assertTrue(arr[1].compare(day_info3))
        self.assertTrue(arr[2].compare(day_info4))

    # tests if the first date is smaller than the range and the second date is within the range but not included
    def test_lookup_range_begin_to_not_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        arr = db.lookup_range(datetime.datetime(2005,2,28,5),datetime.datetime(2005,3,4,5))

        self.assertEqual(len(arr),4)

        self.assertTrue(arr[0].compare(day_info1))
        self.assertTrue(arr[1].compare(day_info2))
        self.assertTrue(arr[2].compare(day_info3))
        self.assertTrue(arr[3].compare(day_info4))

    # tests if the first date is within the range but not included and the second date is greater than the range
    def test_lookup_range_not_included_to_end(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        day_info4 = Day_Info(datetime.datetime(2005,3,4),10,4)
        day_info5 = Day_Info(datetime.datetime(2005,3,5),6,5)
        day_info6 = Day_Info(datetime.datetime(2005,3,6),9,6)

        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        db.add_entry(day_info4)
        db.add_entry(day_info5)
        db.add_entry(day_info6)

        arr = db.lookup_range(datetime.datetime(2005,3,2,5),datetime.datetime(2005,3,7,5))

        self.assertEqual(len(arr),4)

        self.assertTrue(arr[0].compare(day_info3))
        self.assertTrue(arr[1].compare(day_info4))
        self.assertTrue(arr[2].compare(day_info5))
        self.assertTrue(arr[3].compare(day_info6))

# testing parse_file function within statistics tool
class TestParseFile(unittest.TestCase):

    # tests for correct functionality of database
    def test_parse_file(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\sample_test.txt",db), 0)

    # test parse_file function if the correct error code is returned if the filename is not valid
    def test_parse_file_filename(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        self.assertEqual(parse_file("test_files\\not_real_file_name.txt",db),1)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Could not open file path \" test_files\\not_real_file_name.txt \". "
                         "Make sure file is in correct directory\n",capture.getvalue())


    # test parse_file function if the correct error code is returned if the dates within the file are not valid
    def test_parse_file_date(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        self.assertEqual(parse_file("test_files\\incorrect_dates.txt", db), 2)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Error in parsing. Make sure in line 2 the time is in ISO-8061 format\n",capture.getvalue())

    # test parse_file function if the correct error code is returned if the prices within the file are not valid
    def test_parse_file_price(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        self.assertEqual(parse_file("test_files\\incorrect_prices.txt",db), 3)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Error in parsing. Make sure in line 4 the price is a valid value\n",capture.getvalue())


    # test parse_file function if the correct error code is returned if the units within the file are not valid
    def test_parse_file_units(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        self.assertEqual(parse_file("test_files\\incorrect_units.txt", db), 4)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Error in parsing. Make sure in line 3 the number of "
                         "units is a valid value\n",capture.getvalue())

# testing the search_db function within statistics tool
class TestSearchDB(unittest.TestCase):

    # tests search_db function if correct error code is returned when database is empty
    def test_search_db_empty(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\empty_file.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val,0)

        self.assertEqual(search_db(datetime.datetime(2005,3,2,1),db),5)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("File has no entries therefore cannot return information\n",capture.getvalue())

    # tests search_db function if correct error code is returned when function is given invalid datetime
    def test_search_db_comparison(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)
        self.assertEqual(search_db(3,db),6)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Object given is <class 'int'> and cannot be "
                         "compared to a datetime object\n",capture.getvalue())

    # tests search_db if the correct code is returned when the datetime is less than the range of the database
    def test_search_db_datetime_less(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)
        self.assertEqual(search_db(datetime.datetime(2005,1,2,3),db),0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Datetime object given is smaller than the smallest entry found in the file. "
              "Returning information about smallest item\nPrice at 2017-03-01 13:37:59+00:00 : 21.37\n",capture.getvalue())

    # tests search_db if the correct code is returned when the datetime is greater than the range of the database
    def test_search_db_datetime_greater(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)

        self.assertEqual(search_db(datetime.datetime(2020,1,2,3),db),0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Datetime object given is larger than the largest entry found in the file. "
         "Returning information about largest item\nPrice at 2017-06-12 09:51:21+00:00 : 17.21\n",capture.getvalue())

    # tests search_db if the correct code is returned when the datetime is included in the database
    def test_search_db_datetime_included(self):
        db = Database()
        
        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)
        self.assertEqual(search_db(datetime.datetime(2017,6,12,9,51,21),db),0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Price at 2017-06-12 09:51:21+00:00 : 17.21\n",capture.getvalue())


    # tests search_db if the correct code is returned when the datetime is not included in the database
    def test_search_db_datetime_not_included(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)
        self.assertEqual(search_db(datetime.datetime(2017,5,31),db),0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Price at 2017-05-31 00:00:00+00:00 : 20.15\n",capture.getvalue())

# testing get_statistics function within Statistics tool
class TestGetStatistics(unittest.TestCase):

    # tests get_statistics if the database is empty
    def test_get_statistics_empty(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\empty_file.txt", db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)

        self.assertEqual(get_statistics(datetime.datetime(2000, 1, 2, 3), datetime.datetime(2020, 1, 2, 3), db), 7)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("File has no entries therefore cannot return information\n",capture.getvalue())

    # tests get_statistics if the statistics are correct when the range of dates provided encompass all entries
    def test_get_statistics_all(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)

        self.assertEqual(get_statistics(datetime.datetime(2000,1,2,3),datetime.datetime(2020,1,2,3),db),0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("Average Price:  20.46\nMinimum Price:  17.21\n"
                         "Maximum Price:  23.09\nMedian Units:  77.50\n"
                         "Standard Deviation of Units: 34615.62\n",capture.getvalue())

    # tests get_statistics if the statistics are correct when the range of dates provided encompasses one entry
    def test_get_statistics_one(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt",db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)

        self.assertEqual(get_statistics(datetime.datetime(2017,5,14,3),datetime.datetime(2017,5,30,3),db),0)

        # reset23.09 21
        sys.stdout = sys.__stdout__

        self.assertEqual("Average Price:  23.09\nMinimum Price:  23.09\n"
                         "Maximum Price:  23.09\nMedian Units:  21.00\n"
                         "Standard Deviation of Units: 0.00\n", capture.getvalue())

    # tests get_statistics if the statistics are correct when the range of the dates provided encompasses no entries
    def test_get_statistics_none(self):
        db = Database()

        # redirect stdout to capture
        capture = StringIO()
        sys.stdout = capture

        val = parse_file("test_files\\sample_test.txt", db)

        # ensures parse_file is working correctly
        self.assertEqual(val, 0)

        self.assertEqual(get_statistics(datetime.datetime(2017, 5, 14, 3), datetime.datetime(2017, 5, 18, 3), db), 0)

        # reset
        sys.stdout = sys.__stdout__

        self.assertEqual("No entries in the file within the given dates. Giving information about adjacent dates.\n"
                         "Price at 2017-05-18 03:00:00+00:00 : 21.63\n",capture.getvalue())


if __name__ == '__main__':
    unittest.main()

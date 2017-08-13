import unittest
import datetime
from statistics_tool import parse_file, search_db
from database import Database
from day_info import Day_Info

# testing day_info functions
class TestDI(unittest.TestCase):

    def test_get_date(self):

        di = Day_Info(datetime.datetime(2005,1,2,3,4),100,2)

        self.assertEqual(datetime.datetime(2005,1,2,3,4),di.get_date())

    def test_get_price(self):

        di = Day_Info(datetime.datetime(2005, 1, 2, 3, 4), 100, 2)

        self.assertEqual(100, di.get_price())

    def test_get_quantity(self):

        di = Day_Info(datetime.datetime(2005, 1, 2, 3, 4), 100, 2)

        self.assertEqual(2, di.get_quantity())

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

    def test_compare_different_quantity(self):

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

class TestStatisticsTool(unittest.TestCase):

    # tests for correct functionality of database
    def test_parse_file(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\sample_test.txt",db), 0)
        

    # test parse_file function if the correct error code is returned if the filename is not valid
    def test_parse_file_filename(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\not_real_file_name.txt",db),1)

    # test parse_file function if the correct error code is returned if the dates within the file are not valid
    def test_parse_file_date(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\incorrect_dates.txt", db), 2)

    # test parse_file function if the correct error code is returned if the prices within the file are not valid
    def test_parse_file_price(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\incorrect_prices.txt",db), 3)

    # test parse_file function if the correct error code is returned if the units within the file are not valid
    def test_parse_file_units(self):
        db = Database()

        self.assertEqual(parse_file("test_files\\incorrect_units.txt", db), 4)





if __name__ == '__main__':
    unittest.main()
import unittest
import datetime
from database import Database
from day_info import Day_Info

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
        self.assertEqual(2,3)


class TestDB(unittest.TestCase):

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

        self.assertEqual(inside[0].get_date(), day_info1.get_date())
        self.assertEqual(inside[1].get_date(), day_info2.get_date())
        self.assertEqual(inside[2].get_date(), day_info3.get_date())
        self.assertEqual(inside[3].get_date(), day_info4.get_date())
        self.assertEqual(inside[4].get_date(), day_info5.get_date())
        self.assertEqual(inside[5].get_date(), day_info6.get_date())

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

        self.assertEqual(inside[0].get_date(), day_info1.get_date())
        self.assertEqual(inside[1].get_date(), day_info2.get_date())
        self.assertEqual(inside[2].get_date(), day_info3.get_date())
        self.assertEqual(inside[3].get_date(), day_info4.get_date())
        self.assertEqual(inside[4].get_date(), day_info5.get_date())
        self.assertEqual(inside[5].get_date(), day_info6.get_date())

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

        self.assertEqual(tup[0].get_date(),day_info2.get_date())
        self.assertEqual(tup[1].get_date(),day_info2.get_date())

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

        self.assertEqual(tup[0].get_date(),day_info1.get_date())
        self.assertEqual(tup[1].get_date(),day_info2.get_date())

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

        self.assertEqual(tup[0].get_date(),day_info1.get_date())
        self.assertEqual(tup[1].get_date(),day_info1.get_date())

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
        self.assertEqual(arr[0].get_date(), day_info3.get_date())
        self.assertEqual(arr[1].get_date(), day_info4.get_date())
        self.assertEqual(arr[2].get_date(), day_info5.get_date())

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

        self.assertEqual(arr[0].get_date(), day_info1.get_date())
        self.assertEqual(arr[1].get_date(), day_info2.get_date())
        self.assertEqual(arr[2].get_date(), day_info3.get_date())
        self.assertEqual(arr[3].get_date(), day_info4.get_date())
        self.assertEqual(arr[4].get_date(), day_info5.get_date())
        self.assertEqual(arr[5].get_date(), day_info6.get_date())

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

        self.assertEqual(arr[0].get_date(), day_info2.get_date())
        self.assertEqual(arr[1].get_date(), day_info3.get_date())
        self.assertEqual(arr[2].get_date(), day_info4.get_date())


if __name__ == '__main__':
    unittest.main()
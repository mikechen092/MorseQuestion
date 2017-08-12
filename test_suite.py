import unittest
import datetime
from database import Database
from day_info import Day_Info

class TestDB(unittest.TestCase):

    def test_lookup_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),6,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),7,3)
        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)


        self.assertEqual(db.lookup(datetime.datetime(2005,3,2)),day_info2.get_price())

    def test_lookup_not_included(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,1)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),20,2)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),50,3)
        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)


        self.assertEqual(db.lookup(datetime.datetime(2005,3,1,5)),12.5)


    def test_add_in_order(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,10)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),5,10)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),5,10)
        db.add_entry(day_info1)
        db.add_entry(day_info2)
        db.add_entry(day_info3)
        inside = db.db

        self.assertEqual(inside[0].get_date(),day_info1.get_date())
        self.assertEqual(inside[1].get_date(), day_info2.get_date())
        self.assertEqual(inside[2].get_date(), day_info3.get_date())

    def test_add_out_of_order(self):
        db = Database()

        day_info1 = Day_Info(datetime.datetime(2005,3,1),5,10)
        day_info2 = Day_Info(datetime.datetime(2005,3,2),5,10)
        day_info3 = Day_Info(datetime.datetime(2005,3,3),5,10)

        db.add_entry(day_info3)
        db.add_entry(day_info2)
        db.add_entry(day_info1)
        inside = db.db

        self.assertEqual(inside[0].get_date(),day_info1.get_date())
        self.assertEqual(inside[1].get_date(), day_info2.get_date())
        self.assertEqual(inside[2].get_date(), day_info3.get_date())

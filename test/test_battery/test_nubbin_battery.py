import unittest 
from datetime import date 

from battery.Nubin_battery import NubinBattery

class Test_Nubin_Battery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-10-22")
        last_service_date = date.fromisoformat("2018-10-23")
        battery = NubinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-06-20")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
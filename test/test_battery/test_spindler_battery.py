import unittest 
from datetime import date 

from battery.Spindler_battery import SpindlerBattery

class Test_Nubin_Battery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2022-10-22")
        last_service_date = date.fromisoformat("2020-10-23")
        battery = SpindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2022-06-20")
        last_service_date = date.fromisoformat("2021-01-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
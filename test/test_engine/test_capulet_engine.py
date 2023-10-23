import unittest

from engine.capulet_engine import CapuletEngine


class Test_Capulet_engine(unittest.TestCase):
    def needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def does_not_need_service(self):
        current_mileage = 30000
        last_service_mileage = 0 
        engine = CapuletEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())


import unittest

from engine.willoughby_engine import WilloughbyEngine


class Test_Capulet_engine(unittest.TestCase):
    def needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def does_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 0 
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        self.assertFalse(engine.needs_service())

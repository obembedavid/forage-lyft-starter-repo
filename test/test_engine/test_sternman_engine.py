import unittest

from engine.sternman_engine import SternmanEngine


class Test_Sternman_engine(unittest.TestCase):
    def needs_service(self):
        warning_light_on = False 
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())
    
    def does_not_need_service(self):
        warning_light_off = True
        engine = SternmanEngine(warning_light_off)
        self.assertFalse(engine.needs_service())

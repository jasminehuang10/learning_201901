import unittest
from learning.city_functions import city_country

class NameTestCase(unittest.TestCase):
    """测试city_functions.py"""
    def test_city_country(self):
        get_city_country=city_country("shanghai","china")
        self.assertEqual(get_city_country,"Shanghai,China")



unittest.main()



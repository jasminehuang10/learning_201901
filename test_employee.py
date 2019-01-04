
import unittest
from learning.city_functions import Employee

class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        name=("jasmine","huang")
        self.employee=Employee(name)
        self.response=[("jasmine"+" "+"huang"+ "5000"),("jasmine"+" "
                                                                  ""+"huang"+" "+Employee.salary)]
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertIn(self.employee)



import unittest 
from  parameterized import parameterized_class
from apps.program import add,sub,multiply

@parameterized_class(('a','b','expected_sum','expected_diff'),(
    (1, 2, 3, -1),
   (5, 7, 12, -2),
   (9,9,18,0),
))

class TestProgram(unittest.TestCase):
    def test_add(self):
      self.assertEqual(add(self.a,self.b), self.expected_sum)

    def test_sub(self):
      self.assertEqual(sub(self.a,self.b), self.expected_diff)
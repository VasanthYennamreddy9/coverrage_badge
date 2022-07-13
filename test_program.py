import unittest 
from  parameterized import parameterized_class

@parameterized_class(('a','b','expected_sum','expected_diff'),(
    (1, 2, 3, -1),
   (5, 7, 12, 2),
))

class TestProgram(unittest.TestCase):
    def test_add(self):
      self.assertEqual(self.a + self.b, self.expected_sum)

    def test_sub(self):
      self.assertEqual(self.a * self.b, self.expected_diff)
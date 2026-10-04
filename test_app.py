import unittest
from app import sum
class testapp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(2,3),5)
if __name__=="__main__":
    unittest.main()
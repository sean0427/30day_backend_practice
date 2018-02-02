import os
import unittest

from shop import app
from shop.model.Number import Number

class NumberModelTests(unittest.TestCase):
    def test_query(self):
        result = Number.query.all()
        print(result)

if __name__ == '__main__':
    unittest.main()

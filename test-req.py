import unittest
import request
from test_cases import test_cases
import sys



class TestRequestTask(unittest.TestCase):

    def test_check_names(self):
        res = []
        for name in test_cases.names['name']:
            res.append(request.check_name(name))
        self.assertEqual(test_cases.names['res'], res)


if __name__ == '__main__':
    unittest.main()
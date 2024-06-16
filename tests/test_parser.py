import unittest
from camel_case_parser.parser import dict_snake

class TestModule(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(dict_snake({'fistName':'Jobi'}), {'fist_name':'Jobi'})

if __name__ == "__main__":
    unittest.main()
import unittest

def format_name_as_first_last(first_name, last_name):
    return first_name + ' ' + last_name

def format_name_as_first_mid_last(first_name, middle_name, last_name):
    return first_name + ' ' + middle_name + ' ' + last_name 

class TestNameFormatting(unittest.TestCase):
    def test_format_name_as_first_last(self):
        self.assertEqual(format_name_as_first_last('John', 'Doe'), 'John Doe')

    def test_format_name_as_first_mid_last(self):
        self.assertEqual(format_name_as_first_mid_last('John', 'Q.', 'Doe'), 'John Q. Doe')

if __name__ == '__main__':
    unittest.main()
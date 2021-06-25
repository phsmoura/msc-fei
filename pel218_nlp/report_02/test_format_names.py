import unittest
from format_names import FormatName


class FormatNameTest(unittest.TestCase):
    def test_lowercase_to_title(self):
        name = FormatName('john doe')
        self.assertEqual(name.title(), "John Doe")
    
    def test_inverse_to_title(self):
        name = FormatName('jOHN dOE')
        self.assertEqual(name.title(), "John Doe")

    def test_more_tha_2_spaces(self):
        name = FormatName('jOHN dOE foO bAR')
        self.assertEqual(name.title(), "John Doe Foo Bar")
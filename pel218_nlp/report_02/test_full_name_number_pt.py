import unittest
from full_number_name_pt import WriteNumber

class WriteNumberTest(unittest.TestCase):
    def test_zero(self):
        n = WriteNumber(0)
        self.assertEqual(n.get_number_name(), "zero")

    def test_3_digits(self):
        n = WriteNumber(327)
        self.assertEqual(n.get_number_name(), "trezentos e vinte e sete")

    def test_2_digits(self):
        n = WriteNumber(38)
        self.assertEqual(n.get_number_name(), "trinta e oito")

    def test_1_digit(self):
        n = WriteNumber(5)
        self.assertEqual(n.get_number_name(), "cinco")

    def test_3_digits_special_case_1st_digit(self):
        n = WriteNumber(127)
        self.assertEqual(n.get_number_name(), "cento e vinte e sete")

    def test_3_digits_special_case_1st_2nd_digit(self):
        n = WriteNumber(115)
        self.assertEqual(n.get_number_name(), "cento e quinze")

    def test_3_digits_special_case_3rd_digit_zero(self):
        n = WriteNumber(120)
        self.assertEqual(n.get_number_name(), "cento e vinte")

    def test_100(self):
        n = WriteNumber(100)
        self.assertEqual(n.get_number_name(), "cem")

    def test_10(self):
        n = WriteNumber(10)
        self.assertEqual(n.get_number_name(), "dez")

    def test_2_digits_special_case(self):
        n = WriteNumber(13)
        self.assertEqual(n.get_number_name(), "treze")

    def test_2_digits_special_case_2nd_digit_zero(self):
        n = WriteNumber(20)
        self.assertEqual(n.get_number_name(), "vinte")
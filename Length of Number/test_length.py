from length_num import number_length
import unittest

class TestNumbers(unittest.TestCase):

    def test_number(self):
        self.assertEqual(number_length(111), 3)

    def test_number_1(self):
        self.assertEqual(number_length(11), 2)

    def test_number_2(self):
        self.assertEqual(number_length(10000000000), 11)

    def rais_er(self):
        with self.assertRaises(ValueError) as cm:
            number_length(000)
        self.assertEqual('test', cm.exception.args[0])

if __name__ == '__main__':
    unittest.main()
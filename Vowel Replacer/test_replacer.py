import unittest
from replacer import replace_vowels

class TestReplace(unittest.TestCase):

    def test_replace(self):
        self.assertEqual(replace_vowels("the aardvark", "#"), "th# ##rdv#rk")

    def test_replace_1(self):
        self.assertEqual(replace_vowels("minnie mouse", "?"), "m?nn?? m??s?")

if __name__ == '__main__':
    unittest.main()
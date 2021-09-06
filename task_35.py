"""
Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid
Examples

relation_to_luke("Darth Vader") ➞ "Luke, I am your father."

relation_to_luke("Leia") ➞ "Luke, I am your sister."

relation_to_luke("Han") ➞ "Luke, I am your brother in law."
"""
import unittest

dict_fam = {
    'Darth Vader': 'father',
    'Leia': 'sister',
    'Han': 'brother in law',
    'R2D2': 'droid'
}


def relation_to_luke(name):
    return 'Luke, I am your'+ " " + dict_fam[name]+"."


print(relation_to_luke('Leia'))
# name = ["Darth Vader", "Leia", "Han", "R2D2"]
# result = ["Luke, I am your father.", "Luke, I am your sister.", "Luke, I am your brother in law.",
#           "Luke, I am your droid."]
#
#
# class Test_work(unittest.TestCase):
#     def test_relation_to_luke(self):
#         self.assertEqual(relation_to_luke("Darth Vader"), "Luke, I am your father.")
#
#     def test_relation_to_luke1(self):
#         self.assertEqual(relation_to_luke("Leia"), "Luke, I am your sister.")
#
#
# unittest.main()

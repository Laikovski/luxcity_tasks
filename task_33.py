"""
Create a function that takes two arguments: the original price and the discount percentage as integers
 and returns the final price after the discount.

Alternative Text
Examples

dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
"""
def dis(price, discount):
    return round(price - round(((price/100) * discount), 2), 2)
print(dis(1500, 50))
print(dis(89, 20))
print(dis(100, 75))
print(dis(593, 61))

# Test.assert_equals(dis(100, 75), 25)
# Test.assert_equals(dis(211, 50), 105.5)
# Test.assert_equals(dis(593, 61), 231.27)
# Test.assert_equals(dis(1693, 80), 338.6)
# Test.assert_equals(dis(700, 10), 630)

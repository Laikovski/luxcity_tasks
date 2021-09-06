"""
Imagine you took all the numbers between 0 and n and concatenated them together into a long string.
How many digits are there between 0 and n? Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10 and there are 189 digits between 0 and 100.
"""

def digits(number):
    res = (len(str(x)) for x in range(number))
    return sum(res) - 1

print(digits(100))
# print(digits(10))
# print(digits(2020))
print(digits(58473029386609125789))
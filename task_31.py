"""
Create a function that takes two numbers and a mathematical operator + - / * and will perform a
calculation with the given numbers.
Examples

calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
"""

def calculator(num1, operator, num2):
    arr = [num1, operator, num2]
    try:
        return int(eval(''.join(str(x) for x in arr)))
    except:
        return "Can't divide by 0!"

print(calculator(2, "+", 2))
print(calculator(2, "*", 2))
print(calculator(4, "/", 2))
print(calculator(2, "/", 0))
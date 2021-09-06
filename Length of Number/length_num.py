'''
Create a function that takes a number num and returns its length.
Examples

number_length(10) ➞ 2
number_length(5000) ➞ 4
number_length(0) ➞ 1

Notes
The use of the len() function is prohibited.
'''

def number_length(num):
    res = 0
    if type(num) is int:
        for _ in str(num):
           res += 1
    else:
        raise ValueError('Ошибка input')

    return res



# print(number_length(10))
# print(number_length(5000))
# print(number_length(1))
# print(number_length('dddd'))
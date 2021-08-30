"""
The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"

The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones.
Your function should return the number described above.
"""

# def consecutive_zeros(str):
#     num_arr = [0]
#     res = 0
#     for i in str:
#         if i == '0':
#             res += 1
#         else:
#             num_arr.append(res)
#             res = 0
#     num_arr.append(res)
#     return max(num_arr)

def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result

print(consecutive_zeros('1001101000111'))
print(consecutive_zeros('1'))
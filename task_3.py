"""
For a given string s find the character with longest consecutive repetition and return number of consecutive
repetition :

In the input:

    s - string

 At the output: number
"""

def get_number_of_repetitions(s):
    set = 0
    for i in s:
        c = s.count(i)
        if c > set:
            set = c
    return set

print(get_number_of_repetitions("qqqzxdd"))
print(get_number_of_repetitions("ddff"))
print(get_number_of_repetitions(""))
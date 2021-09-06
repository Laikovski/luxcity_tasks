'''
Create a function that replaces all the vowels in a string with a specified character.
Examples

replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
'''

def replace_vowels(txt, ch):
    res =''
    for i in txt:
        if i in 'aeiuyo':
            res += ch
        else:
            res += i
    return res
# print(replace_vowels("the aardvark", "#"))
# print(replace_vowels("minnie mouse", "?"))
# print(replace_vowels("shakespeare", "*"))
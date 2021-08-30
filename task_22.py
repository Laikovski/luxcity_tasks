"""
Define a function named triple_and that takes three parameters and returns True only
if they are all True and False otherwise.
"""

def triple_and(a, b, c):
    return all([a, b, c])

print(triple_and(1,2,3))
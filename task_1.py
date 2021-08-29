"""
Planks of different colors were used to build a fence. String “ fence” describes the fence. Different letters represent boards of a unique color. Write a function that defines the  largest  space between boards of the same color. If there are no boards of the same color then return -1.

 Input:

    fence - string - a fence made of boards, each letter is a separate board

 Output:  integer - the number of different color boards between boards of the same color (used boards of the same color are not taken into account)

 Note :

    all Latin letters in lower case
"""

def get_result(fence):
    s = []
    for i, n in enumerate(fence):
        if fence.count(n) > 1:
            s.append(i)
        else:
            continue
    if len(s) == 0:
        return -1
    elif len(s) == 2:
        return abs(s[0]-s[1])-1
    else:
        return abs(s[1] - s[2]) - 1


print(get_result("davcaef"))
print(get_result("qweq"))
print(get_result("aabcadef"))
print(get_result("pp"))
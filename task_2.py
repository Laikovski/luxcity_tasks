"""
The personnel department has special wishes for the candidates' qualities - requirements.
Each letter in requirements represents a unique wish. For the i-th candidate there is data on
the mentions of his qualities in the resume - candidates[i]. Only those candidates who have indicated
any  qualities from the requirements and no others are invited for an interview.

 Input:
    requirements - string
    candidates - strings array

 Output:  integer - number of candidates invited for the interview

 Note:
    requirements.length> 0
    candidates.length> 0
    candidates[i] consists of lowercase Latin letters
    letters in requirements are not repeating
"""

def get_result(requirements, candidates):
    res = 0
    for i in candidates:
        if i in requirements:
            res += 1
    return res
requirements = "aduj"
candidates = ["u"," okp","jo","adujo","du","a"]

print(get_result (requirements, candidates))
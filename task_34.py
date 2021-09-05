"""
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is
pronounced with a question mark ?.
Examples

stutter("incredible") ➞ "in... in... incredible?"

stutter("enthusiastic") ➞ "en... en... enthusiastic?"

stutter("outstanding") ➞ "ou... ou... outstanding?"
"""
import unittest
def stutter(word):
    return (word[0:2]) + '...'+' '+ (word[0:2])+'...'+ ' ' +(word)+'?'

print(stutter("incredible"))
print(stutter("enthusiastic"))
print(stutter("outstanding"))


class TestWork(unittest.TestCase):

    self.actual_param = [
	"increasing", "adventures", "enticing", "unacceptable", "accountable", "incredible", "exquisite",
	"am", "enduring", "outstanding", "astonishing", "astounding", "impressive", "revolutionize",
	"recurring", "recollection", "so", "gorgeous", "captivating"
]
    self.expected_param = [
	"in... in... increasing?", "ad... ad... adventures?", "en... en... enticing?", "un... un... unacceptable?",
    "ac... ac... accountable?", "in... in... incredible?", "ex... ex... exquisite?", "am... am... am?",
    "en... en... enduring?", "ou... ou... outstanding?", "as... as... astonishing?", "as... as... astounding?",
    "im... im... impressive?", "re... re... revolutionize?", "re... re... recurring?", "re... re... recollection?",
    "so... so... so?", "go... go... gorgeous?", "ca... ca... captivating?",
]

    def test_stuter(self):
        for i, w in enumerate(self.actual_param):
            self.assertEquals(stutter(w), self.expected_param[i])


unittest.main()

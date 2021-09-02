"""
Reverse Words

Easy

Given a string s of words delimited by spaces, reverse the order of words.

Constraints

    n ≤ 100,000 where n is the length of s

Example 1
Input

sentence = "hello there my friend"

Output

"friend my there hello"
"""


class Solution:
    def solve(self, sentence):
        nlist = []
        nlist = sentence.split()
        nlist.reverse()
        rslt = " ".join(nlist)
        return rslt


        

"""
Pseudocode
unitialize a empty list = new_list
split the sentence an put it in a list
reverse list
result = join list and leReverse Words

Easy

Given a string s of words delimited by spaces, reverse the order of words.

Constraints

    n ≤ 100,000 where n is the length of s

Example 1
Input

sentence = "hello there my friend"

Output

"friend my there hello"ave an space
return result
"""
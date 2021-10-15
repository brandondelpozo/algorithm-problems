"""
Minimum Bracket Addition

Easy

Given a string s containing brackets ( and ), return the minimum number of brackets that can be inserted so that the brackets are balanced.
Minimum Bracket Addition
Constraints

    n ≤ 100,000 where n is the length of s

Example 1
Input

s = ")))(("
s1 = "))(()"
Output

5

Explanation

We can insert ((( to the front and )) to the end
"""

class Solution:
    def solve(self, s):
        cnt1, cnt2 = 0, 0
        for char in s:
            if char == "(":
                cnt1 += 1
            else:
                if cnt1:
                    cnt1 -= 1
                else:
                    cnt2 += 1
        return cnt1 + cnt2
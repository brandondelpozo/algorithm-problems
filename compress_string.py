"""
Compress String - easy
Given a string lowercase alphabet s, eliminate consecutive duplicate characters from the string and return it.

That is, if a list contains repeated characters, they should be replaced with a single copy of the character. The order of the elements should not be changed.

Constraints

    0 ≤ n ≤ 100,000 where n is the length of s

Example 1
Input

s = "aaaaaabbbccccaaaaddf"

Output

"abcadf"

Example 2
Input

s = "a"

Output

"a"

Hint:
Try maintaining 2 pointers to remove the duplicates in place.
"""
#Solution
class Solution:
    def solve(self, s):
        lst = []
        prev = None
        for i in s:
            if not prev or prev != i:
                lst.append(i)
            prev = i
        return "".join(lst)
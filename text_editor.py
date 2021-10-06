"""
Problem name: Text Editor

leve: Easy

Instructions:
Given a string s representing characters typed into an editor, with "<-" representing a backspace, return the current state of the editor.

Constraints

    n ≤ 100,000 where n is the length of s

Example 1
Input

s = "abc<-z"

Output

"abz"

Explanation

The "c" got deleted by the backspace.
Example 2
Input

s = "<-x<-z<-"

Output

""

Explanation

All characters are deleted. Also note you can type backspace when the editor is empty as well.
"""


class Solution:
    def solve(self, s):
        text = s.split("<-")
        ans = text[0]
        for i in range(1, len(text)):
            ans = ans[:-1]  # removing last character
            ans += text[i]
        return ans


"""
Solution:

Intuition

Split the given string sss using delimiter as '<-'. Proceed as in example below.
Implementation

def solve(self, s):
    text = s.split("<-") # splitting the string s
    ans = text[0]
    for i in range(1, len(text)):
        ans = ans[:-1]  # removing last character
        ans += text[i]  # appending to the ans
    return ans

Example #1

Input : "abc<-z"

After splitting , text = ['abc', 'z']

Initialize the string to store edited text:
ans = text[0] // ans = 'abc'

Traverse the remaining list and keep removing the last character of ans:

for i in range(1,len(text)):
    ans = ans[:-1] // ans = 'ab'
    ans = ans + text[i] // ans = 'abz'

ans will store the final edited string.
Time Complexity

O(n)\mathcal{O}(n)O(n): Time taken for splitting the given string sss (O(n))( \mathcal{O}(n) )(O(n)) + time taken for traversing the resultant list after splitting (O(n))( \mathcal{O}(n) )(O(n)); (where nnn is the length of the given string sss)
Space Complexity

O(n)\mathcal{O}(n)O(n): After splitting, the resultant list size will be less than or equal to n/2n/2n/2

"""
"""
Sum of Two Numbers

Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. You may not use the same element twice.

Note: Numbers can be negative or 0.

Constraints

    n ≤ 100,000 where n is the length of nums

Example 1
Input

nums = [35, 8, 18, 3, 22]

k = 11

Output

True

Explanation

8 + 3 = 11
Example 2
Input

nums = [10, 36, 22, 14]

k = 4

Output

False

Explanation

No two numbers in this list add up to 4.
Example 3
Input

nums = [24, 10, 11, 4]

k = 15

Output

True

Explanation

11 + 4 = 15
Example 4
Input

nums = [-22, 22, -11, 11]

k = 0

Output

True

Explanation

-11 + 11 = 0
Example 5
Input

nums = [15, 0, 3, 2]

k = 15

Output

True

Explanation

15 + 0 = 15

"""

class Solution:
    def solve(self, nums, k):
        s = set()
        for e in nums:
            if k - e in s:
                return True
            s.add(e)
        return False



"""
Solution interpretation:

Intuition
It is a very easy problem which is basically searching for an integer number in the nums array.

Implementation
In the code, the set takes all the already visited values.
Time Complexity

Here the time complexity is O(n) as there is only a simple for loop.O(n)\mathcal{O}(n)O(n)

Space Complexity
Here arrays are used that is why it is O(n) and others are normal variables 1 unit of storage.O(n)\mathcal{O}(n)O(n)

"""
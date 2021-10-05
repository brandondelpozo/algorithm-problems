"""
Merging Two Sorted Lists
Easy
Given two lists of integers a and b sorted in ascending order, merge them into one large sorted list.

Constraints

    0 ≤ n ≤ 200,000 where n is the length of a
    0 ≤ m ≤ 200,000 where m is the length of b

Example 1
Input

a = [5, 10, 15]

b = [3, 8, 9]

Output

[3, 5, 8, 9, 10, 15]
"""

class Solution:
    def solve(self, a, b):
        ai, bi, result = 0, 0, []
        while ai < len(a) and bi < len(b):
            if a[ai] <= b[bi]:
                result.append(a[ai])
                ai += 1
            else:
                result.append(b[bi])
                bi += 1

        return result + a[ai:] + b[bi:]

"""
Intuition

Since both of the input collections are sorted, we can just work from front-to-back over both collections and take the minimum remaining from each of the collections. Once one of the collections has been entirely consumed, we can just stick the remaining items onto the end of the result because they must be greater (and already sorted).
Implementation

We maintain a pointer into each collection and append the minimum at each step of the way. Once a collection has been entirely consumed, we can just stick the rest of the remaining items on the result because they must all be greater (and already sorted).
Time Complexity

O(n)\mathcal{O}(n)O(n) Each item in the input lists will produce exactly one comparison, append, and increment.
Space Complexity

O(n)\mathcal{O}(n)O(n) The only storage required is a pair of ints and a list that will contain the same elements as the two input collections.

"""
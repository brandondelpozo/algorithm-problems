"""Add One to List

Easy

You are given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].

For example, [1, 3, 9] represents the number 139.

Return the same list in the same representation except modified so that 1 is added to the number.

Constraints

    1 ≤ n ≤ 100,000 where n is the length of nums.

Example 1
Input

nums = [1, 9, 1]

Output

[1, 9, 2]

Example 2
Input

nums = [9]

Output

[1, 0]"""

# Solution
class Solution:
    def solve(self, nums):
        i = len(nums) - 1
        while i >= 0:
            if nums[i] + 1 <= 9:
                nums[i] = nums[i] + 1
                break
            else:
                nums[i] = 0
            i -= 1
        if i < 0:
            nums.insert(0, 1)
        return nums


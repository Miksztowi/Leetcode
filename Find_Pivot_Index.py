# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal
# to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes,
# you should return the left-most pivot index.
# Example 1:
# Input:
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:
# Input:
# nums = [1, 2, 3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
# Note:
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].

# Leetcode Weekly Contest 58.
# 741 / 741 test cases passed.
# Status: Accepted
# Runtime: 59 ms
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        left_sum, right_num = 0, sum(nums)
        for i, num in enumerate(nums):
            right_num -= num
            if left_sum == right_num:
                return i
            left_sum += num
        else:
            return -1

# how to handle the negative.

if __name__ == '__main__':
    print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
    print(Solution().pivotIndex([0, 0, 0, 0]))
    print(Solution().pivotIndex([1, 2, 3]))
    print(Solution().pivotIndex([-1, -1, -1, -1, 0, 1]))
    print(Solution().pivotIndex([1, 1, -1]))
    print(Solution().pivotIndex([1]))

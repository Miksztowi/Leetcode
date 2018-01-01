# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Example 1
# Input: [3,0,1]
# Output: 2
# Example 2
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 122 / 122 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 91.71 % of python submissions.
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # right_sum = sum(range(len(nums) + 1)) Bad !
        n = len(nums)
        right_sum = n * (n + 1) // 2
        return right_sum - sum(nums)


# 122 / 122 test cases passed.
# Status: Accepted
# Runtime: 49 ms
# Your runtime beats 50.18 % of python submissions.
from functools import reduce
from operator import xor
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return reduce(xor, nums) ^ [n, 1, n + 1, 0][n % 4]


if __name__ == '__main__':
    print(Solution().missingNumber([3, 0, 1]))
    print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))

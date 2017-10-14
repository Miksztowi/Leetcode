# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.
# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        dummy = {0: 1}
        res = sum_ = 0
        for num in nums:
            sum_ += num
            res += dummy.get(sum_ - k, 0)
            dummy[sum_] = dummy.get(sum_, 0) + 1

        return res


if __name__ == '__main__':
    print(Solution().subarraySum([-1, -1, 1], 1))
    print(Solution().subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))


# 80 / 80 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 86.08 % of python submissions.

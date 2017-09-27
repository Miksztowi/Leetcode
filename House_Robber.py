# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.
# Also thanks to @ts for adding additional test cases.


# Here is Greedy Algorithm.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0

        for i in nums:
            last, now = now, max(last + i, now)
            print(i, last, now)

        return now


# Here is the DP formula that leads to the right answer:
# M(k) = money at the kth house
# P(0) = 0
# P(1) = M(1)
# P(k) = max(P(k−2) + M(k), P(k−1))
# Coding by: __Gan__
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        lo, hi = 2, len(nums)
        k_1, k = nums[0], max(nums[0], nums[1])
        while lo < hi:
            k_2, k_1 = k_1, k
            k = max(k_2 + nums[lo], k_1)
            lo += 1
        return k


if __name__ == '__main__':
    # print(Solution().rob([1,2,1,3]))
    # print(Solution().rob([1]))
    # print(Solution().rob([2,1]))
    print(Solution().rob([2,1,2,4]))
    print(Solution().rob([0, 0]))
    print(Solution().rob([1, 1, 1]))


# 69 / 69 test cases passed.
# Status: Accepted
# Runtime: 29 ms
# Your runtime beats 90.61 % of python submissions.

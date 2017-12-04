# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Note: This is an extension of House Robber.
# After robbing those houses on that street, the thief has found himself a new place for his thievery
# so that he will not get too much attention. This time, all houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses
# remain the same as for those in the previous street.
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

# 74 / 74 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Your runtime beats 28.27 % of python submissions.
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

        len_orgin = len(nums)
        # No matter what results from the first iteration, the second iteration always results the correct.
        # i.e. [2, 3, 2] -- > [2, 3, 2, 2, 3, 2] , answer is 3 .That is second iteration result.
        nums = nums + nums

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1] - dp[len_orgin - 1]


# 74 / 74 test cases passed.
# Status: Accepted
# Runtime: 28 ms
# Your runtime beats 90.79 % of python submissions.
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

        def linerob(nums):
            last, now = 0, 0
            for i in range(len(nums)):
                last, now = now, max(last + nums[i], now)

            return now

        return max(
            (linerob(nums[1:])),
            (linerob(nums[:-1]))
        )


if __name__ == '__main__':
    print(Solution().rob([2, 1, 2, 4]))
    print(Solution().rob([2, 1, 1, 1]))
    print(Solution().rob([2, 1]))
    print(Solution().rob([0, 0]))
    print(Solution().rob([1, 1, 1]))
    print(Solution().rob([1]))
    print(Solution().rob([]))

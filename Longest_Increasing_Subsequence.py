# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an unsorted array of integers, find the length of longest increasing subsequence.
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.


# 24 / 24 test cases passed.
# Status: Accepted
# Runtime: 1468 ms
# Your runtime beats 6.41 % of python submissions.
# DP Formula: DP[i] = max(DP[j] + 1, DP[i]), nums[j] is all numbers that bigger than the nums[i].
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = len(nums) * [1]
        for i in range(len(nums), -1, -1):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS([10,9,2,5,3,4]))
    print(Solution().lengthOfLIS([]))

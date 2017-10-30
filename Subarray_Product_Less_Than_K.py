# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Contest 55.
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays
# where the product of all the elements in the subarray is less than k.
# Example 1:
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Note:
# 0 < nums.length <= 50000.
# 0 < nums[i] < 1000.
# 0 <= k < 10^6.


# 84 / 84 test cases passed.
# Status: Accepted
# Runtime: 332 ms
# Your runtime beats 59.09 % of python submissions.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1 or not nums:
            return 0
        ans = left = 0
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            while product >= k:  # Use left to generate new subset.
                product /= nums[left]
                left += 1
            ans += i - left + 1

        return ans


if __name__ == '__main__':
    print(Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100))
    print(Solution().numSubarrayProductLessThanK([1,1,1], 2))

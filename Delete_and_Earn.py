# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array nums of integers, you can perform operations on the array.
# In each operation, you pick any nums[i] and delete it to earn nums[i] points.
# After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.
# You start with 0 points. Return the maximum number of points you can earn by applying such operations.
# Example 1:
# Input: nums = [3, 4, 2]
# Output: 6
# Explanation:
# Delete 4 to earn 4 points, consequently 3 is also deleted.
# Then, delete 2 to earn 2 points. 6 total points are earned.
# Example 2:
# Input: nums = [2, 2, 3, 3, 3, 4]
# Output: 9
# Explanation:
# Delete 3 to earn 3 points, deleting both 2's and the 4.
# Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
# 9 total points are earned.
# Note:
# The length of nums is at most 20000.
# Each element nums[i] is an integer in the range [1, 10000].

# Leetcode Weekly Contest 61.
# 46 / 46 test cases passed.
# Status: Accepted
# Runtime: 132 ms
# DP Formula:
# DP[0] = nums[0]
# DP[1] = max(nums[0], nums[1])
# DP[k] = max(DP[k - 2] + value, DP[k - 1])
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        points, pre, cur = [0] * 10001, 0, 0
        for num in nums:
            points[num] += num
        for p in points:
            pre, cur = cur, max(pre + p, cur)
        return cur


if __name__ == '__main__':
    # print(Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]))
    # print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]))
    # print(Solution().deleteAndEarn([2, 2]))
    # print(Solution().deleteAndEarn([3, 1]))
    # print(Solution().deleteAndEarn([3, 4, 2]))
    # print(Solution().deleteAndEarn([8, 7, 3, 8, 1, 4, 10, 10, 10, 2]))
    print(Solution().deleteAndEarn(
        [12, 32, 93, 17, 100, 72, 40, 71, 37, 92, 58, 34, 29, 78, 11, 84, 77, 90, 92, 35, 12, 5, 27, 92, 91, 23, 65, 91,
         85, 14, 42, 28, 80, 85, 38, 71, 62, 82, 66, 3, 33, 33, 55, 60, 48, 78, 63, 11, 20, 51, 78, 42, 37, 21, 100, 13,
         60, 57, 91, 53, 49, 15, 45, 19, 51, 2, 96, 22, 32, 2, 46, 62, 58, 11, 29, 6, 74, 38, 70, 97, 4, 22, 76, 19, 1,
         90, 63, 55, 64, 44, 90, 51, 36, 16, 65, 95, 64, 59, 53, 93]
    ))

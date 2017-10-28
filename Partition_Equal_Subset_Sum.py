# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty array containing only positive integers,
# find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
# Input: [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# Input: [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.


# Solution like one-dimensional array to solve 01 knapsack problem.
# http://love-oriented.com/pack/P01.html
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 802 ms
# Your runtime beats 70.14 % of python submissions.
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ % 2:
            return False
        target = sum_ // 2
        memo = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                memo[i] = memo[i] or memo[i - num]
        return memo[target]


# DFS
# 104 / 104 test cases passed.
# Status: Accepted
# Runtime: 38 ms
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # If the num is greater than the target, it should return False and break loop.
        # Otherwise, when nums = [1] * 98 + [100] will cost 98! * 97! * 96! * ... * 1! times calculation. Abhorrent!
        nums.sort(reverse=True)
        sum_ = sum(nums)
        if sum_ % 2:
            return False

        def canPartitionRec(nums, start, end, target):
            if target == 0:
                return True
            for i in range(start, end):
                if target < nums[i]:
                    return False
                if canPartitionRec(nums, i + 1, end, target - nums[i]):
                    return True
            return False

        return canPartitionRec(nums, 0, len(nums), sum_ // 2)


if __name__ == '__main__':
    # print(Solution().canPartition(nums=[1] * 18 + [20]))
    # print(Solution().canPartition(nums=[1, 2, 3, 5]))
    # print(Solution().canPartition(nums=[1, 3, 4, 4]))
    print(Solution().canPartition(nums=[1,2,3,4,5,6,7]))
    # print(Solution().canPartition(nums=[71,70,66,54,32,63,38,98,4,22,61,40,6,8,6,21,71,36,30,34,44,60,89,53,60,56,73,14,63,37,15,58,51,88,88,32,80,32,10,89,67,29,68,65,34,15,88,8,57,78,37,63,73,65,47,39,32,74,31,44,43,4,10,8,96,22,58,87,29,99,79,13,96,21,62,71,34,55,72,3,96,7,36,64,30,6,14,87,12,90,40,13,29,21,94,33,99,86,4,100]))
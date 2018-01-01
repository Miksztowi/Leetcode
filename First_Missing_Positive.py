# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an unsorted integer array, find the first missing positive integer.
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# Your algorithm should run in O(n) time and uses constant space.

# 156 / 156 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 10.42 % of python submissions.
# Put each number in its right place.
# For example:
# When we find 5, then swap it with A[4].
# At last, the first place where its number is not right, return palce + 1.
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, i = len(nums), 0

        while i < n:
            if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > n:
                i += 1
            elif nums[nums[i] - 1] != nums[i]:
                tmp = nums[i] - 1
                nums[i], nums[tmp] = nums[tmp], nums[i]
            else:
                i += 1
        i = 0
        while i < n and nums[i] == i + 1:
            i += 1
        return i + 1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([1, 2, 0]))

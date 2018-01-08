# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
# Return true if there exists i, j, k
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
# Given [5, 4, 3, 2, 1],
# return false.
#
# Credits:
# Special thanks to @DjangoUnchained for adding this problem and creating all test cases.


# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 38 ms
# Your runtime beats 44.24 % of python submissions.
# Start with the maximum numbers for the first and second element. Then:
# (1) Find the first smallest number in the 3 subsequence
# (2) Find the second one greater than the first element, reset the first one if it’s smaller
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        first = second = float('inf')
        for i in range(len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                return True
        return False


if __name__ == '__main__':
    print(Solution().increasingTriplet([1, 2, 3, 4, 5]))
    print(Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4]))

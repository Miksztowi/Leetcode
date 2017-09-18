# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
# Your algorithm's runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return [-1, -1].
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) < 1:
            return [-1, -1]

        def search(compare_func, nums, target):
            lo, hi = 0, len(nums) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if compare_func(nums[mid], target):
                    hi = mid - 1
                else:
                    lo = mid + 1
            return lo

        lo = search(lambda x, y: x >= y, nums, target)
        if lo >= len(nums) or nums[lo] != target:
            # In python, A or B, if A is True,it won't judge the B.
            # But A | B, if A is True, it still judge the B.
            # And  'and' '&' is the same.
            return [-1, -1]
        hi = search(lambda x, y: x > y, nums, target)
        return [lo, hi - 1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(Solution().searchRange([1], 1))
    print(Solution().searchRange([2, 2], 3))

# 87 / 87 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Your runtime beats 32.40 % of python submissions

# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array and a value, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example:
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.


# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 79.57 % of python submissions.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo, hi = 0, len(nums)
        while lo < hi:
            if nums[lo] == val:
                nums[lo:] = nums[lo + 1:]
                hi -= 1
                lo -= 1
            lo += 1
        return len(nums)


# 113 / 113 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 2.24 % of python submissions.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        new_length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_length] = nums[i]
                new_length += 1
        return new_length


if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 3))
    print(Solution().removeElement([3, 3], 3))

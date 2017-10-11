# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array nums, write a function to move all 0's
# to the end of it while maintaining the relative order of the non-zero elements.
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 239 ms
# Your runtime beats 13.95 % of python submissions.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        move_times = nums.count(0)
        for i in range(move_times):
            nums.pop(nums.index(0))
            nums += 0,


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 85 ms
# Your runtime beats 24.24 % of python submissions.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 58 ms
# Your runtime beats 79.77 % of python submissions.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        move_times = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[move_times] = nums[i]
                move_times += 1

        while move_times < len(nums):
            nums[move_times] = 0
            move_times += 1
        print(nums)


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 0, 3, 12]))
    print(Solution().moveZeroes([0, 1]))


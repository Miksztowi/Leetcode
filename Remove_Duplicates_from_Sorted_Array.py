# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
# Example:
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


# 161 / 161 test cases passed.
# Status: Accepted
# Runtime: 129 ms
# Your runtime beats 11.88 % of python submissions.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            if nums[lo] == nums[lo + 1]:
                temp = lo
                duplication_length = 0
                while temp < hi and nums[temp] == nums[temp + 1]:
                    duplication_length += 1
                    temp += 1
                hi -= duplication_length
                nums[lo:temp + 1] = [nums[lo]]
            lo += 1

        return len(nums)


# 161 / 161 test cases passed.
# Status: Accepted
# Runtime: 82 ms
# Your runtime beats 56.07 % of python submissions.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        new_length = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[new_length]:
                new_length += 1
                nums[new_length] = nums[i]
        # New nums = nums[:new_length + 1]
        return new_length + 1

if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 1, 2]))

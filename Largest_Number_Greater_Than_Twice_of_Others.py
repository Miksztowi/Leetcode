# -*- encoding:utf-8 -*-
# __author__=='Gan'

# In a given integer array nums, there is always exactly one largest element.
# Find whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, otherwise return -1.
# Example 1:
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
# Note:
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].


# LeetCode Weekly Contest 64.
# Find the max and the second max.
# 244 / 244 test cases passed.
# Status: Accepted
# Runtime: 28 ms
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return nums[0]
        largest = max(nums)
        for num in nums:
            if num != 0 and num != largest and largest // num < 2:
                return -1
        return nums.index(largest)


# 244 / 244 test cases passed.
# Status: Accepted
# Runtime: 55 ms
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return -1 if any(filter(lambda x: x * 2 > max(nums) if x != max(nums) else False, nums)) else nums.index(
            max(nums))


if __name__ == '__main__':
    print(Solution().dominantIndex([3, 6, 1, 0]))
    print(Solution().dominantIndex([1, 2, 3, 4]))

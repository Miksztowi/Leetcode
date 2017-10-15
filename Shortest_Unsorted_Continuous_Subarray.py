# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in
# ascending order, then the whole array will be sorted in ascending order, too.
# You need to find the shortest such subarray and output its length.
# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.


# 307 / 307 test cases passed.
# Status: Accepted
# Runtime: 152 ms
# Your runtime beats 9.42 % of python submissions.
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(''.join(['.',' '][m==n] for m,n in zip(nums, sorted(nums))).strip())


# 307 / 307 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Your runtime beats 93.72 % of python submissions.
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right and nums[left] <= nums[left+1]:
            left += 1
        if left == right:
            return 0
        while right > 0 and nums[right] >= nums[right-1]:
            right -= 1

        max_ = max(nums[left:right+1])
        min_ = min(nums[left:right+1])

        while left >= 0 and nums[left] > min_:
            left -= 1
        while right < len(nums) and nums[right] < max_:
            right += 1

        return right - left - 1


# 307 / 307 test cases passed.
# Status: Accepted
# Runtime: 156 ms
# Your runtime beats 8.92 % of python submissions.
# 1.nums[0, i - 1] and nums[j + 1, n - 1] are both sorted.
# 2.nums[i] != nums_sorted[i] and nums[j] != nums_sorted[j].
# 3.nums[i - 1] <= min and max <= nums[j + 1],
# where min and max are the minimum and maximum values of subarray nums[i, j].
# https://discuss.leetcode.com/topic/93391/ideas-behind-the-o-n-two-pass-and-one-pass-solutions
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, -1
        max_ = float('-inf')
        min_ = float('inf')
        for i in range(len(nums)):
            max_ = max(max_, nums[i])
            if nums[i] != max_:
                right = i

            min_ = min(min_, nums[len(nums) - i - 1])
            if nums[len(nums) - i - 1] != min_:
                left = len(nums) - i - 1

        return right - left + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(Solution().findUnsortedSubarray([4, 6, 8, 10, 2]))
    print(Solution().findUnsortedSubarray([1,2,3,4]))
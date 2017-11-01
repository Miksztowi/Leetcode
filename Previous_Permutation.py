# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a list of integers, which denote a permutation.
# Find the previous permutation in ascending order.
#  Notice
# The list may contains duplicate integers.
# For [1,3,2,3], the previous permutation is [1,2,3,3]
# For [1,2,3,4], the previous permutation is [4,3,2,1]


# Find Pivot --> Reverse nums from pivot to high -- >
# If Pivot > 0: Find the first number smaller than nums[pivot - 1], exchange them value.
class Solution(object):
    def previousPermuation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums) == 1:
            return nums
        # O(n)
        if nums[-1] < nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return nums

        lo, hi = 0, len(nums) - 1
        pivot = hi
        while lo < pivot and nums[pivot - 1] <= nums[pivot]:
            pivot -= 1

        reverse_index = pivot
        while reverse_index < hi:
            nums[reverse_index], nums[hi] = nums[hi], nums[reverse_index]
            hi -= 1
            reverse_index += 1

        if pivot:
            swap_index = pivot
            while swap_index <= hi and nums[swap_index] >= nums[pivot - 1]:
                swap_index += 1
            print(pivot)
            nums[swap_index], nums[pivot - 1] = nums[pivot - 1], nums[swap_index]

        return nums


if __name__ == '__main__':
    # print(Solution().previousPermuation([3, 2, 1]))
    # print(Solution().previousPermuation([1, 1, 5]))
    # print(Solution().previousPermuation([1, 3, 2]))
    print(Solution().previousPermuation([1, 2, 3, 4]))
    # print(Solution().previousPermuation([1, 2]))
    # print(Solution().previousPermuation([4, 3, 1, 2]))

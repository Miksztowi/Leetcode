# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


# Find Pivot --> Reverse nums from pivot to high -- >
# If Pivot > 0: Find the first number smaller than nums[pivot - 1], exchange them value.
# 265 / 265 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Your runtime beats 33.74 % of python submissions.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        lo, hi = 0, len(nums) - 1

        while lo < hi:
            if nums[hi - 1] < nums[hi]:
                change_index = hi
                for i in range(len(nums) - 1, hi - 1, -1):
                    if nums[hi - 1] < nums[i]:
                        change_index = i
                        break
                nums[hi - 1], nums[change_index] = nums[change_index], nums[hi - 1]
                nums[hi:] = reversed(nums[hi:])
                return
            hi -= 1
        nums.reverse()


# 265 / 265 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 60.80 % of python submissions.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        # O(1)
        if nums[-1] > nums[-2]:
            nums[-1], nums[-2] = nums[-2], nums[-1]
            return
        lo, pivot, hi = 0, len(nums) - 1, len(nums) - 1
        while lo < pivot and nums[pivot - 1] >= nums[pivot]:
            pivot -= 1

        reverse_index = pivot
        while reverse_index < hi:
            nums[reverse_index], nums[hi] = nums[hi], nums[reverse_index]
            reverse_index += 1
            hi -= 1

        swap_index = pivot
        if pivot > 0:
            while swap_index <= hi and nums[swap_index] <= nums[pivot - 1]:
                swap_index += 1

            nums[swap_index], nums[pivot - 1] = nums[pivot - 1], nums[swap_index]

        print(nums)


if __name__ == '__main__':
    print(Solution().nextPermutation([3, 2, 1]))
    print(Solution().nextPermutation([1, 1, 5]))
    print(Solution().nextPermutation([1, 3, 2]))
    print(Solution().nextPermutation([4, 3, 1, 2]))
    print(Solution().nextPermutation([1, 3, 2, 4]))
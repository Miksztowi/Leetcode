# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


# MLE !
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def findkth(nums, k):
            if len(nums) <= 1:
                return nums[0]
            larger_list = []
            smaller_list = []
            for i in nums[1:]:
                if i > nums[0]:
                    larger_list.append(i)
                else:
                    smaller_list.append(i)
            if len(larger_list) == k - 1:
                return nums[0]
            elif len(larger_list) > k - 1:
                return findkth(larger_list, k)
            else:
                return findkth(smaller_list, k - len(larger_list) - 1)
        return findkth(nums, k)

# The Idea of Quick Sort
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, lo, hi):
            axis = nums[lo]
            while lo < hi:
                while hi > lo and nums[hi] > axis:
                    hi -= 1
                while hi > lo and nums[lo] < axis:
                    lo += 1
                if lo <= hi:
                    nums[lo], nums[hi] = nums[hi], nums[lo]
                else:
                    break
            return lo

        while True:
            lo = partition(nums, 0, len(nums) - 1)
            if len(nums) - lo == k:
                return nums[lo]
            elif len(nums) - lo > k:
                lo += 1
                nums = nums[lo:]
            else:
                k -= (len(nums) - lo)
                nums = nums[:lo]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return []
        else:
            pivot = nums[0]
            less = [x for x in nums if x < pivot]
            large = [x for x in nums if x > pivot]
            equal = [x for x in nums if x == pivot]
            k -= len(equal)
            rank = len(large)
            if rank == k:
                return pivot
            elif rank > k:
                return self.findKthLargest(large, k)
            else:
                return self.findKthLargest(less, k - rank)



if __name__ == '__main__':
    # print(Solution().findKthLargest([1, 2, 3], 3))
    # print(Solution().findKthLargest([1], 1))
    # print(Solution().findKthLargest([7,6,5,4,3,2,1], 2))
    # print(Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 9))
    print(Solution().findKthLargest([5,2,4,1,3,6,0], 4))

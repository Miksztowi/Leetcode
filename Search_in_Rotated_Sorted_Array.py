# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif (nums[lo] <= nums[mid] and nums[lo] <= target < nums[mid]) \
                or (nums[lo] > nums[mid] and not (nums[mid] < target <= nums[hi])):
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

if __name__ == '__main__':
    print(Solution().search([3, 5, 1], 3))
    print(Solution().search([1], 3))


# 196 / 196 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 52.69 % of python submissions.

# Use XHR to handle different situation.
# Explanation
# My solutions use binary search guided by the following thoughts:
#
# Remember the array is sorted, except it might drop at one point.
#
# If nums[0] <= nums[i], then nums[0..i] is sorted (in case of "==" it's just one element,
# and in case of "<" there must be a drop elsewhere).
#  So we should keep searching in nums[0..i] if the target lies in this sorted range,
#  i.e., if nums[0] <= target <= nums[i].
# If nums[i] < nums[0], then nums[0..i] contains a drop,
# and thus nums[i+1..end] is sorted and lies strictly between nums[i] and nums[0].
# So we should keep searching in nums[0..i] if the target doesn't lie strictly between them, i.e.,
# if target <= nums[i] < nums[0] or nums[i] < nums[0] <= target
# Those three cases look cyclic:
#     nums[0] <= target <= nums[i]
#                target <= nums[i] < nums[0]
#                          nums[i] < nums[0] <= target
# So I have the three checks (nums[0] <= target),
# (target <= nums[i]) and (nums[i] < nums[0]),
# and I want to know whether exactly two of them are true.
# They can't all be true or all be false (check it),
# so I just need to distinguish between "two true" and "one true".
# Parity is enough for that, so instead of adding them I xor them,
# which is a bit shorter and particularly helpful in Java and Ruby,
# because those don't let me add booleans but do let me xor them.
# (Actually while developing this I thought of permutations of nums[0],
# target and nums[i] and the permutation parity and saw those three checks as representing inversions,
# but I had trouble putting that into words and now find the above explanation much better.
# But it helped me get there, so I wanted to mention it here.)
# Python:
def search(self, nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) / 2
        if (nums[0] > target) ^ (nums[0] > nums[mid]) ^ (target > nums[mid]):
            lo = mid + 1
        else:
            hi = mid
    return lo if target in nums[lo:lo+1] else -1

# Python using bisect:
import bisect
class Solution:
    def search(self, nums, target):
        self.__getitem__ = lambda i: \
            (nums[0] <= target) ^ (nums[0] > nums[i]) ^ (target > nums[i])
        i = bisect.bisect_left(self, True, 0, len(nums))
        return i if target in nums[i:i+1] else -1


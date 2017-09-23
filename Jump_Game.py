# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
# For example:
# A = [2,3,1,1,4], return true.
# A = [3,2,1,0,4], return false.


# TLE!
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        now = 0
        while True:
            max_index = now + nums[now]
            interval = nums[now]
            if max_index >= len(nums) - 1:
                return True
            elif interval == 0:
                return False
            for i in range(interval + 1):
                now += 1
                if now >= len(nums) - 1:
                    return True
                if max_index <= (nums[now] + now):
                    break


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False
        last = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last <= 0


if __name__ == '__main__':
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([2, 0]))
    print(Solution().canJump([1,1,2,2,0,1,1]))
    print(Solution().canJump([5,9,3,2,1,0,2,3,3,1,0,0]))


# Solution 1
# Going forwards. m tells the maximum index we can reach so far.
# def canJump(self, nums):
#     m = 0
#     for i, n in enumerate(nums):
#         if i > m:
#             return False
#         m = max(m, i+n)
#     return True


# Solution 2
# One-liner version:
# def canJump(self, nums):
#     return reduce(lambda m, (i, n): max(m, i+n) * (i <= m), enumerate(nums, 1), 1) > 0


# Solution 3
# Going backwards, most people seem to do that, here's my version.
# def canJump(self, nums):
#     goal = len(nums) - 1
#     for i in range(len(nums))[::-1]:
#         if i + nums[i] >= goal:
#             goal = i
#     return not goal

# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return ''
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return nums[i - 1]
        return nums[-1]


if __name__ == '__main__':
    print(Solution().singleNumber([1,2,3,2,3]))


# 15 / 15 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 48.89 % of python submissions.


# Here is so cool !!!!
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a ^= num # XOR, Ex: 3 ^ 3 = 0.
        return a


# But it's better not to use extra space
def singleNumber3(self, nums):
    return 2*sum(set(nums))-sum(nums)


from functools import reduce
def singleNumber4(self, nums):
    return reduce(lambda x, y: x ^ y, nums)

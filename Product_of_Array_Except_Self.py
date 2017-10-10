# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of n integers where n > 1, nums,
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# Solve it without division and in O(n).
# For example, given [1,2,3,4], return [24,12,8,6].
# Follow up:
# Could you solve it with constant space complexity?
# (Note: The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        left_product = [nums[0]]
        right_product = [nums[-1]]
        res = []
        for i in range(2, len(nums)):
            left_product.append(nums[i - 1] * left_product[-1])
            right_product.append(nums[-i] * right_product[-1])
        for i in range(len(left_product) - 1):
            res.append(left_product[i] * right_product[-(i + 2)])
        return [right_product[-1]] + res + [left_product[-1]]

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dummy = 1
        res = []
        for i in range(len(nums)):
            res.append(dummy)
            dummy *= nums[i]
        dummy = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= dummy
            dummy *= nums[i]
        return res

if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
    print(Solution().productExceptSelf([1, 2]))


# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 169 ms
# Your runtime beats 44.49 % of python submissions.

# !! notice !!
# In range(N+1)[::-1], the first doing the exact same thing as range(N, -1, -1) and then inverting the list.
# That's why it takes more time.
# In [12]: %timeit(range(100+1)[::-1])
# 657 ns ± 6.88 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
# In [13]: %timeit(range(100, -1, -1))
# 385 ns ± 2.98 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of numbers nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that appear only once.
# For example:
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
# Note:
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 46.73 % of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        ans = []
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i-1] != nums[i]:
                ans += nums[i-1],
                nums.insert(i, nums[i])
                if len(ans) == 2:
                    return ans
        return ans + [nums[-1]]


# Once again, we need to use XOR to solve this problem. But this time, we need to do it in two passes:
# In the first pass, we XOR all elements in the array,
# and get the XOR of the two numbers we need to find. Note that since the two numbers are distinct,
# so there must be a set bit (that is, the bit with value '1') in the XOR result. Find
# out an arbitrary set bit (for example, the rightmost set bit).
# In the second pass, we divide all numbers into two groups, one with the aforementioned bit set,
# another with the aforementinoed bit unset.
# Two different numbers we need to find must fall into thte two distrinct groups. XOR numbers in each group,
# we can find a number in either group.
# A Corner Case:
# When diff == numeric_limits<int>::min(), -diff is also numeric_limits<int>::min().
# Therefore, the value of diff after executing diff &= -diff is still numeric_limits<int>::min().
#  The answer is still correct.

# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 77.88 % of python submissions.
from functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        diff = reduce(lambda x, y: x ^ y, nums)
        diff &= -diff  # Find the rightmost 1.

        ans = [0] * 2
        for num in nums:
            if num & diff:
                ans[0] ^= num
            else:
                ans[1] ^= num
        return ans




if __name__ == '__main__':
    print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))
    print(Solution().singleNumber([0, 1, 1, 2]))
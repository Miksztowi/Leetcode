# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of integers, every element appears three times except for one,
# which appears exactly once. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


# 11 / 11 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 50.10 % of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        for i in range(1, len(nums), 3):
            if nums[i-1] != nums[i+1]:
                return nums[i-1] if nums[i+1] == nums[i] else nums[i+1]

        return nums[-1]


# 11 / 11 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 59.06 % of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for i in nums:
            b=(b^i)&~a
            a=(a^i)&~b
        return b


# 11 / 11 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 50.10 % of python submissions.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1 = x2 = 0
        for num in nums:
            x2 ^= x1 & num
            x1 ^= num
            mask = ~(x1 & x2)
            # If x1=1 and x2=1, then mask = -2.
            # And -2 & 1 = 0.So mask can reset the counter when count equals k.
            print(x1, x2, mask)
            x1 &= mask
            x2 &= mask

        return x1

if __name__ == '__main__':
    print(Solution().singleNumber([1, 1, 1, 2, 3, 2, 2]))
    # print(Solution().singleNumber([1, 1, 1, 2, 2, 2, 3]))


# https://discuss.leetcode.com/topic/11877/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
# Here is a list of few quick examples to show how the algorithm works:
# k = 2, p = 1
# k is 2, then m = 1, we need only one 32-bit integer(x1) as the counter.
    # And 2^m = k so we do not even need a mask! A complete java program will look like:
#     public int singleNumber(int[] A) {
#          int x1 = 0;
#
#          for (int i : A) {
#              x1 ^= i;
#          }
#
#          return x1;
#     }
# k = 3, p = 1
# k is 3, then m = 2, we need two 32-bit integers(x2, x1) as the counter.
    # And 2^m > k so we do need a mask. Write k in its binary form: k = '11',
    # then k1 = 1, k2 = 1, so we have mask = ~(x1 & x2). A complete java program will look like:
#     public int singleNumber(int[] A) {
#          int x1 = 0, x2 = 0, mask = 0;
#
#          for (int i : A) {
#              x2 ^= x1 & i;
#              x1 ^= i;
#              mask = ~(x1 & x2);
#              x2 &= mask;
#              x1 &= mask;
#          }
#
#          return x1;  // p = 1, in binary form p = '01', then p1 = 1, so we should return x1;
#                      // if p = 2, in binary form p = '10', then p2 = 1, so we should return x2.
#     }
# k = 5, p = 3
# k is 5, then m = 3, we need three 32-bit integers(x3, x2, x1) as the counter.
    #  And 2^m > k so we need a mask. Write k in its binary form: k = '101',
    # then k1 = 1, k2 = 0, k3 = 1, so we have mask = ~(x1 & ~x2 & x3). A complete java program will look like:
#     public int singleNumber(int[] A) {
#          int x1 = 0, x2 = 0, x3  = 0, mask = 0;
#
#          for (int i : A) {
#              x3 ^= x2 & x1 & i;
#              x2 ^= x1 & i;
#              x1 ^= i;
#              mask = ~(x1 & ~x2 & x3);
#              x3 &= mask;
#              x2 &= mask;
#              x1 &= mask;
#          }
#
#          return x1;  // p = 3, in binary form p = '011', then p1 = p2 = 1, so we can
#                      // return either x1 or x2. But if p = 4, in binary form p = '100',
#                      // only p3 = 1, which implies we can only return x3.
#     }

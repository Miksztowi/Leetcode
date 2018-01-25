# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits),
# and its complement is 0. So you need to output 0.


# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 51 ms
# Your runtime beats 4.98 % of python submissions.
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        complement = {'1': '0', '0': '1'}
        return int(''.join(complement[x] for x in bin(num)[2:]), 2)


# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 18.41 % of python submissions.
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i <<= 1
        return (i - 1) ^ num  # Because there is no leading zero.


if __name__ == '__main__':
    print(Solution().findComplement(5))
    print(Solution().findComplement(0))

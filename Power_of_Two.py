# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an integer, write a function to determine if it is a power of two.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 1108 / 1108 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 19.16 % of python submissions.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        answer = 1
        while answer < n:
            answer <<= 1
        return answer == n


# 1108 / 1108 test cases passed.
# Status: Accepted
# Runtime: 43 ms
# Your runtime beats 32.84 % of python submissions.
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n < 1 else n & (n - 1) == 0  # power of two should contain only one bit.


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(2))
    print(Solution().isPowerOfTwo(3))
    print(Solution().isPowerOfTwo(0))

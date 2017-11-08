# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Write a program to check whether a given number is an ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.
# Note that 1 is typically treated as an ugly number.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

# Factor
# 1012 / 1012 test cases passed.
# Status: Accepted
# Runtime: 98 ms
# Your runtime beats 50.00 % of python3 submissions.
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for p in [2, 3, 5]:
            while num % p == 0 and num > 0:
                num /= p

        return num == 1


if __name__ == '__main__':
    print(Solution().isUgly(6))
    print(Solution().isUgly(6))

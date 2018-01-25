# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# Example:
# Given num = 16, return true. Given num = 5, return false.
# Follow up: Could you solve it without loops/recursion?
# Credits:
# Special thanks to @yukuairoy for adding this problem and creating all test cases.


# 1060 / 1060 test cases passed.
# Status: Accepted
# Runtime: 43 ms
# Your runtime beats 35.38 % of python submissions.
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        answer = 1
        while answer < num:
            answer <<= 2
        return answer == num


# 1060 / 1060 test cases passed.
# Status: Accepted
# Runtime: 43 ms
# Your runtime beats 35.38 % of python submissions.
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and num & (num - 1) == 0 and (num - 1) % 3 == 0


if __name__ == '__main__':
    print(Solution().isPowerOfFour(1))
    print(Solution().isPowerOfFour(2))
    print(Solution().isPowerOfFour(4))
    print(Solution().isPowerOfFour(48))

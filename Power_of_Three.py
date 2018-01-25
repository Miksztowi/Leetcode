# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an integer, write a function to determine if it is a power of three.
# Follow up:
# Could you do it without using any loop / recursion?
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# 21038 / 21038 test cases passed.
# Status: Accepted
# Runtime: 263 ms
# Your runtime beats 25.66 % of python submissions.
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1162261467 is 3^19,  3^20 is bigger than int
        return 1162261467 % n == 0 and n > 0


if __name__ == '__main__':
    print(Solution().isPowerOfThree(1))
    print(Solution().isPowerOfThree(3))
    print(Solution().isPowerOfThree(6))
    print(Solution().isPowerOfThree(9))
    print(Solution().isPowerOfThree(2))

# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1, 2 ... n steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        return sum(self.climbStairs(n - x) for x in range(1, n + 1))

# Solution: Bit manipulation
# Jumping or not for each stairs, except the last one is must to climb. So there are 2^(n - 1) ways to climb.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 << (n - 1)


if __name__ == '__main__':
    print(Solution().climbStairs(3))


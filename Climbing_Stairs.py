# -*- encoding:utf-8 -*-
# __author__=='Gan'

# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.


# bottom - top
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for i in range(n):
            a, b = b, a+b
        return a


# cache!
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cached = {
            0: 1,
            1: 1,
        }

        def fib(num):
            if cached.get(num):
                return cached[num]
            else:
                cached[num] = fib(num - 1) + fib(num - 2)
                return cached[num]
        return fib(n)


if __name__ == '__main__':
    print(Solution().climbStairs(35))


# 45 / 45 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Your runtime beats 58.95 % of python submissions

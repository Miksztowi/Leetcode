# -*- encoding:utf-8 -*-
# __author__=='Gan'

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
# Note: m and n will be at most 100.


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
           return self.uniquePaths(n, m)

        ways = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                ways[j] += ways[j-1]
                print(ways)
        return ways[n - 1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3,3))


# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 132 ms
# Your runtime beats 1.24 % of python submissions.



# Here is the fastest solution.And five times faster than me.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        num = denom = 1
        k = min(m-1, n-1)
        for i in range(k):
            num *= m-1+n-1-i
            denom *= i+1
        return int(num/denom)
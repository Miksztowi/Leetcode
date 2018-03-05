# -*- encoding:utf-8 -*-
# __author__=='Gan'

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Above is a 3 x 7 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.


# Your runtime beats 100.00 % of python3 submissions.
# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 36 ms
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = DP[i][j - 1] + DP[i - 1][j]
        return DP[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))

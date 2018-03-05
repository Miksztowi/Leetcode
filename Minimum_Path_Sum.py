# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes
# the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
# Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


# Your runtime beats 32.90 % of python submissions.
# 61 / 61 test cases passed.
# Status: Accepted
# Runtime: 67 ms

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        DP = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i != m - 1 and j != n - 1:
                    DP[i][j] = min(DP[i][j + 1], DP[i + 1][j])
                elif i == m - 1 and j != n - 1:
                    DP[i][j] = DP[i][j + 1]
                elif j == n - 1 and i != m - 1:
                    DP[i][j] = DP[i + 1][j]
                DP[i][j] += grid[i][j]
        return DP[0][0]


if __name__ == '__main__':
    print(Solution().minPathSum([[1, 3, 1],
                                 [1, 5, 1],
                                 [4, 2, 1]]))

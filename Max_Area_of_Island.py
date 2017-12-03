# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
# Example 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# Note: The length of each dimension in the given grid does not exceed 50.


# 726 / 726 test cases passed.
# Status: Accepted
# Runtime: 146 ms
# Your runtime beats 32.02 % of python submissions.
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        def dfs(row, col, area):
            if not (0 <= row < rows and 0 <= col < cols) or not grid[row][col]:
                return False
            grid[row][col] = 0
            # If add 1 then dfs the 4-directionally has a little issue that different directionally only added once.
            # So do the add operation as follows.
            return 1 + sum([dfs(row + x, col + y, area) for x, y in ((0, 1), (1, 0), (0, -1), (-1, 0))])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    ans = max(ans, dfs(row, col, 0))
        return ans


# >>> a = 0L
# >>> x1 = a and b
# >>> if a:
#         x2 = b
# else:
#         x2 = 0
#
# >>> x1 is x2
# False
# I do need to use 0L there,
# it doesn't work with 0 because that's among the few cached integers and I appear to be unable to create two
# different 0-objects. But that might be just a CPython implementation detail and not defined by Python in general,
# so maybe in some other Python implementation you could have different 0-objects just like you can have different
# 1234-objects in CPython:
# >>> y1 = 1234
# >>> y2 = 1234
# >>> y1 is y2
# False
# In [471]: a = int.from_bytes(bytes([0]), 'big')
#
# In [472]: a
# Out[472]: 0
#
# In [473]: b = int.from_bytes(bytes([0]), 'big')
#
# In [474]: b
# Out[474]: 0
#
# In [475]: a is b
# Out[475]: False
#
# In [476]: id(a)
# Out[476]: 4444004760
#
# In [477]: id(b)
# Out[477]: 4444004808


if __name__ == '__main__':
    print(Solution().maxAreaOfIsland(
        [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    ))

    print(Solution().maxAreaOfIsland(
        [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1]]
    ))

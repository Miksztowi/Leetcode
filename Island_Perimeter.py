# -*- encoding:utf-8 -*-
# __author__=='Gan'

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes"
# (water inside that isn't connected to the water around the island). One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
# Example:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:


# 5833 / 5833 test cases passed.
# Status: Accepted
# Runtime: 228 ms
# Your runtime beats 93.92 % of python submissions.
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        lands = neighbours = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    lands += 1
                    if col < cols - 1 and grid[row][col + 1]:
                        neighbours += 1
                    if row < rows - 1 and grid[row + 1][col]:
                        neighbours += 1
        return lands * 4 - neighbours * 2


# Boundary and water.
# 5833 / 5833 test cases passed.
# Status: Accepted
# Runtime: 322 ms
# Your runtime beats 55.99 % of python submissions.
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])

        def sub_element(row, col):
            ans = 0
            if row == 0:
                ans += 1
            if row + 1 == rows:
                ans += 1
            if col == 0:
                ans += 1
            if col + 1 == cols:
                ans += 1

            if 0 < row and not grid[row - 1][col]:
                ans += 1
            if row < rows - 1 and not grid[row + 1][col]:
                ans += 1
            if 0 < col and not grid[row][col - 1]:
                ans += 1
            if col < cols - 1 and not grid[row][col + 1]:
                ans += 1
            return ans

        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    ans += sub_element(row, col)
        return ans


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for g in (grid, zip(*grid)):
            for row in g:
                temp = 0
                for block in row:
                    if block == 1:
                        temp = 2
                    else:
                        res += temp
                        temp = 0
                res += temp
        return res


if __name__ == '__main__':
    print(Solution().islandPerimeter(
        [[0, 1, 0, 0],
         [1, 1, 1, 0],
         [0, 1, 0, 0],
         [1, 1, 0, 0]]
    ))
    print(Solution().islandPerimeter(
        [[1, 1],
         [1, 1]]
    ))

    print(Solution().islandPerimeter(
        [[1, 0],
         [0, 1]]
    ))
    print(Solution().islandPerimeter(
        [[1]]
    ))

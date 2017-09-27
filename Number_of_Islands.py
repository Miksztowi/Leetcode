# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
# 11000
# 11000
# 00100
# 00011
# Answer: 3


class Solution(object):
    # def numIslands(self, grid):
    #     """
    #     :type grid: List[List[str]]
    #     :rtype: int
    #     """
    #     if not grid:
    #         return 0
    #
    #     def dfs(row ,col, i, j):
    #         if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] != '1':
    #             return
    #         grid[i][j] = '0'
    #         dfs(row, col, i - 1, j)
    #         dfs(row, col, i + 1, j)
    #         dfs(row, col, i, j - 1)
    #         dfs(row, col, i, j + 1)
    #
    #     grid = [list(r) for r in grid]
    #     row = len(grid)
    #     col = len(grid[0])
    #     count = 0
    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == '1':
    #                 dfs(row, col, i, j)
    #                 count += 1
    #     return count

    # This way is failed in Python3.x, but in Python2.x it's worked.
    # def numIslands(self, grid):
    #     grid = [list(r) for r in grid]
    #     def sink(i, j):
    #         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
    #             grid[i][j] = '0'
    #             map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1))
    #             return 1
    #         return 0
    #     return [sink(i, j) for i in range(len(grid)) for j in range(len(grid[i]))]

    # map() is different between the Python3.x and Python2.x.
    # In Python3.x map() will return the object like <map object at 0x10f4923c8>.
    # And it does not executed until it is used.
    # In Python2.x map() will return the list like [0, 0, 0, 0], it was executed directly.

    # This way is worked in Python3.x.
    def numIslands(self, grid):
        grid = [list(r) for r in grid]

        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


if __name__ == '__main__':
    # print(Solution().numIslands(["11110","11010","11000","00000"]))
    # print(Solution().numIslands(["11010","11010","11000","00001"]))
    print(Solution().numIslands(["111","010","111"]))


# 47 / 47 test cases passed.
# Status: Accepted
# Runtime: 102 ms
# Your runtime beats 82.81 % of python submissions.

def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        root = []

        m, n = len(grid), len(grid[0])
        res = 0
        grid = [list(r) for r in grid]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # print(i, j)
                    print(grid)
                    flag = True
                    if i > 0 and grid[i - 1][j] != '0':
                        flag = False
                        grid[i][j] = root[grid[i - 1][j]]
                    if j > 0 and grid[i][j - 1] != '0':
                        if flag:
                            grid[i][j] = root[grid[i][j - 1]]
                        else:
                            root[grid[i][j - 1]] = grid[i][j]
                        flag = False
                    if flag:
                        print(i, j )
                        grid[i][j] = res
                        root.append(res)
                        res += 1
        return sum(root[i] == i for i in range(len(root)))


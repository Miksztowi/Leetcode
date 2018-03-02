# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map,
# compute the volume of water it is able to trap after raining.
#
# Note:
# Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.
#
# Example:
#
# Given the following 3x6 height map:
# [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
#
# Return 4.


# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 242 ms
# Your runtime beats 33.67 % of python submissions.
# The idea is that we maintain all the points of the current border in a min heap and always choose the point with
# the lowest length. This is actually an optimized searching strategy over the trivial brute force method:
# instead of dfs each point to find the lowest “border” of its connected component, we can always start a search
# from the lowest border and update the points adjacent to it.


import heapq


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        res = 0
        height_heap = []
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    heapq.heappush(height_heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        while height_heap:
            height, i, j = heapq.heappop(height_heap)
            for row, col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= row < m and 0 <= col < n and not visited[row][col]:
                    res += max(0, height - heightMap[row][col])
                    visited[row][col] = 1
                    heapq.heappush(height_heap, (max(height, heightMap[row][col]), row, col))
        return res


if __name__ == '__main__':
    print(Solution().trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]))

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1,
# except those cells in the given list mines which are 0.
# What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign.
# If there is none, return 0.
# An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up,
# down, left, and right, and made of 1s. This is demonstrated in the diagrams below.
# Note that there could be 0s or 1s beyond the arms of the plus sign,
# only the relevant area of the plus sign is checked for 1s.
# Examples of Axis-Aligned Plus Signs of Order k:
# Order 1:
# 000
# 010
# 000
# Order 2:
# 00000
# 00100
# 01110
# 00100
# 00000
# Order 3:
# 0000000
# 0001000
# 0001000
# 0111110
# 0001000
# 0001000
# 0000000
# Example 1:
# Input: N = 5, mines = [[4, 2]]
# Output: 2
# Explanation:
# 11111
# 11111
# 11111
# 11111
# 11011
# In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
# Example 2:
# Input: N = 2, mines = []
# Output: 1
# Explanation:
# There is no plus sign of order 2, but there is of order 1.
# Example 3:
# Input: N = 1, mines = [[0, 0]]
# Output: 0
# Explanation:
# There is no plus sign, so return 0.
# Note:
# N will be an integer in the range [1, 500].
# mines will have length at most 5000.
# mines[i] will be length 2 and consist of integers in the range [0, N-1].
# (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        if N == 1: return 0 if mines else 1
        info = [[[0] * 4 for _ in range(N)] for _ in range(N)]
        res = 0
        s = {(mine[0], mine[1]) for mine in mines}

        for x in range(N):
            for y in range(N):
                if (x, y) not in s:
                    info[x][y][0], info[x][y][1] = 1, 1
                    if x - 1 >= 0: info[x][y][0] = info[x - 1][y][0] + 1  # UP
                    if y - 1 >= 0: info[x][y][1] = info[x][y - 1][1] + 1  # LEFT

        for x in range(N - 1, -1, -1):
            for y in range(N - 1, -1, -1):
                if (x, y) not in s:
                    info[x][y][2], info[x][y][3] = 1, 1
                    if x + 1 < N: info[x][y][2] = info[x + 1][y][2] + 1  # DOWN
                    if y + 1 < N: info[x][y][3] = info[x][y + 1][3] + 1  # RIGHT

                    temp = []
                    temp.append(info[x - 1][y][0] if x - 1 >= 0 else 0)
                    temp.append(info[x][y - 1][1] if y - 1 >= 0 else 0)
                    temp.append(info[x + 1][y][2] if x + 1 < N else 0)
                    temp.append(info[x][y + 1][3] if y + 1 < N else 0)

                    res = max([min(temp) + 1, res])
        return res


if __name__ == '__main__':
    print(Solution().orderOfLargestPlusSign(5, [[4, 2]]))
    print(Solution().orderOfLargestPlusSign(5, [[3, 0], [3, 3]]))
    print(Solution().orderOfLargestPlusSign(5, [[0, 0], [0, 3], [1, 1], [1, 4], [2, 3], [3, 0], [4, 2]]))
    print(Solution().orderOfLargestPlusSign(2, []))
    print(Solution().orderOfLargestPlusSign(1, [[0, 0]]))
    print(Solution().orderOfLargestPlusSign(0, [[0, 0]]))

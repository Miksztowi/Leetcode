# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.
# XX  <- domino
# XX  <- "L" tromino
# X
# Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.
# (In a tiling, every square must be covered by a tile.
# Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
# such that exactly one of the tilings has both squares occupied by a tile.)
# Example:
# Input: 3
# Output: 5
# Explanation:
# The five different ways are listed below, different letters indicates different tiles:
# XYZ XXZ XYY XXY XYY
# XYZ YYZ XZZ XYY XXY
# Note:
# N  will be in range [1, 1000].

# If you write down this recursive sequence and do some calculations, you may find that:
# 5 = 2 * 2 + 1
# 11 = 5 * 2 + 1
# 24 = 11 * 2 + 2
# 53 = 24 * 2 + 5
# 117 = 57 * 2 + 11
# A[N] = A[N-1] * 2 + A[N-3]

# Leetcode Contest 73.
# 39 / 39 test cases passed.
# Status: Accepted
# Runtime: 33 ms
class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        DP = [0] * (N + 1)
        DP[0] = 1
        DP[1] = 1
        for i in range(2, N + 1):
            DP[i] = 2 * DP[i - 1] + DP[i - 3]
        return DP[-1] % int(1e9 + 7)


if __name__ == '__main__':
    print(Solution().numTilings(3))
    print(Solution().numTilings(30))
    print(Solution().numTilings(4))

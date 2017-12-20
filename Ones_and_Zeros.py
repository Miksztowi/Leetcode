# -*- encoding:utf-8 -*-
# __author__=='Gan'


# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand,
# there is an array with strings consisting of only 0s and 1s.
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
# Each 0 and 1 can be used at most once.
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".


# 0-1 Knapsack problem.
# 63 / 63 test cases passed.
# Status: Accepted
# Runtime: 4062 ms
# Your runtime beats 40.85 % of python submissions.
from collections import Counter
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        DP = [[0] * (n + 1) for _ in range(m + 1)]
        for c in (Counter(s) for s in strs):
            c0, c1 = c['0'], c['1']
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    DP[i][j] = max(DP[i][j], DP[i - c0][j - c1] + 1)
        return DP[m][n]


if __name__ == '__main__':
    print(Solution().findMaxForm(['11'], 1, 2))
    print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))

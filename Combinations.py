# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


# Your runtime beats 100.00 % of python3 submissions.
# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 128 ms
from itertools import combinations
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return list(combinations(range(1, n + 1), k))


# Your runtime beats 48.86 % of python3 submissions.
# 27 / 27 test cases passed.
# Status: Accepted
# Runtime: 964 ms
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combs = [[]]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n + 1)]
        return combs


if __name__ == '__main__':
    print(Solution().combine(4, 2))

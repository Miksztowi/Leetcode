# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string S, check if the letters can be rearranged so that two characters that are adjacent
# to each other are not the same.
# If possible, output any possible result.  If not possible, return the empty string.
# Example 1:
# Input: S = "aab"
# Output: "aba"
# Example 2:
# Input: S = "aaab"
# Output: ""
# Note:
# S will consist of lowercase letters and have length in range [1, 500].


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 43 ms
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        res = ""
        pq = []
        c = Counter(S)
        for key, value in c.items():
            heapq.heappush(pq, (-value, key))
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            res += b
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        return '' if len(res) != len(S) else res


if __name__ == '__main__':
    print(Solution().reorganizeString('aab'))
    print(Solution().reorganizeString('aabb'))
    print(Solution().reorganizeString('aaab'))
    print(Solution().reorganizeString(''))
    print(Solution().reorganizeString('a'))

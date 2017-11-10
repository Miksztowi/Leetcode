# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a string S and a string T,
# find the minimum window in S which will contain all the characters in T in complexity O(n).
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

# 268 / 268 test cases passed.
# Status: Accepted
# Runtime: 222 ms
# Your runtime beats 44.98 % of python submissions.
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = collections.Counter(t)
        missing = len(t)
        i = I = J = 0
        for j, v in enumerate(s, 1):
            missing -= need[v] > 0  # Equivalent to if need[v] > 0: missing -= 1
            need[v] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    J = j
                    I = i
        return s[I:J]


if __name__ == '__main__':
    # print(Solution().minWindow(
    #     "ADOBECODEBANC",
    #     "ABC",
    # ))
    print(Solution().minWindow(
        "A",
        "A",
    ))

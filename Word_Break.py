# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code".


# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a set of strings).
#  Please reload the code definition to get the latest changes.


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s or not wordDict:
            return False
        res = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i - len(word) + 1: i + 1] == word and (res[i-len(word)] or i-len(word) == -1):
                    res[i] = True
        return res[-1]

    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]


if __name__ == '__main__':
    print(Solution().wordBreak('leetcode', ['leet', 'code']))
    print(Solution().wordBreak('', ['leet', 'code']))

# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 83.86 % of python submissions.

# How to use BFS to solve this question?

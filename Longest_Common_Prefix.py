# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_ = min(strs, key=len)  # len(str) then get min.Otherwise, will get the smallest in alphabet.
        cur = len(min_)
        i = 0
        while i < len(strs):
            if min_[:cur] != strs[i][:cur]:
                cur -= 1
                i = 0
            else:
                i += 1
        return min_[:cur]


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["bbcb","c","aca"]))
    print(Solution().longestCommonPrefix(["ab","abcc"]))
    print(Solution().longestCommonPrefix(["ab","aa"]))


# 117 / 117 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 71.30 % of python submissions.


# Here are some cool solutions from leetcode.
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
    # For else.
    # When the items are exhausted (which is immediately when the sequence is empty),
            # the suite in the else clause, if present, is executed, and the loop terminates.
    # So use 'break' or 'return' can avoid the 'else'.


# Nice use of reduce().
from functools import reduce


def longestCommonPrefix(self, strs):
    def lcp(s, t):
        if len(s)>len(t):
            s, t = t, s
        for i in range(len(s)):
            if s[i]!=t[i]:
                return s[:i]
        return s
    return reduce(lcp,strs) if strs else ""

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# For example, given s = "aab",
# Return
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]

# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 175 ms
# Your runtime beats 42.93 % of python submissions.
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []

        def generate(s, path):
            if not s:
                ans.append(list(path))
                return
            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    generate(s[i:], (path + [s[:i]]))

        def is_palindrome(str_):
            return str_ == str_[::-1]

        generate(s, [])
        return ans


if __name__ == '__main__':
    print(Solution().partition('aab'))

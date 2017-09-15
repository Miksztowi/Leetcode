# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
# Example:
#
# Input: "cbbd"
#
# Output: "bb"


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return None
        max_length, start = 1, 0
        for i in range(len(s)):
            if i - max_length >=1 and s[i - max_length - 1:i + 1] == s[i - max_length - 1:i + 1][::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >=0 and s[i - max_length:i + 1] == s[i - max_length:i + 1][::-1]:
                start = i - max_length
                max_length += 1
        return s[start:start+max_length]


if __name__ == '__main__':
    print(Solution().longestPalindrome("ccacc"))


# 94 / 94 test cases passed.
# Status: Accepted
# Runtime: 79 ms
# Your runtime beats 97.91 % of python submissions.


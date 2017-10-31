# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
# Example 1:
# Input:s1 = "ab" s2 = "eidbaooo"
# Output:True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


# Generating all permutations will cause Time Limit Exceed.
# So we couldn't use String Permutation Algorithm in this problem.
from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not (s1 or s2):
            return False

        def gen_all_perm(count, path, length):
            if len(path) == length:
                self.paths += path,
                return

            for i in count:
                if count[i]:
                    count[i] -= 1
                    gen_all_perm(count, path + i, length)
                    count[i] += 1

        self.paths = []
        gen_all_perm(Counter(s1), '', len(s1))

        return any([x in s2 for x in self.paths])

# For each window representing a substring of s2 of length len(s1), we want to check if the count of the windows is
# equal to the count of s1. And we can maintain the sliding window from 0 to len(s2), but when sliding index is greater
# than len(s1) we should delete the value of s2[i - len(s1). After, we only need to check if sliding window is equal to
# the target window.Which means both of them have the same count of every value.
# Tips:
# ord()Return the Unicode code point for a one-character string. ord('a') --> 97.
# chr()Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff. chr(97) --> 'a'.
# 102 / 102 test cases passed.
# Status: Accepted
# Runtime: 89 ms
# Your runtime beats 72.07 % of python submissions.
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26

        for x in A:
            target[x] += 1

        sliding_window = [0] * 26
        for i, v in enumerate(B):
            sliding_window[v] += 1
            if i >= len(s1):
                sliding_window[B[i - len(s1)]] -= 1
            if sliding_window == target:
                return True

        return False


if __name__ == '__main__':
    print(Solution().checkInclusion(
        'ba',
        'eidbaooo'
    ))
    print(Solution().checkInclusion(
        "prosperity",
        "properties"
    ))
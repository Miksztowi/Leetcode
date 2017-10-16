# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# Note:
# The input string length won't exceed 1000.


# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 202 ms
# Your runtime beats 57.59 % of python submissions.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(2*len(s)-1):
            left_center = i // 2
            right_center = left_center + i % 2
            while left_center >= 0 and right_center < len(s) and s[left_center] == s[right_center]:
                left_center -= 1
                right_center += 1
                res += 1

        return res


# 130 / 130 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Your runtime beats 97.03 % of python submissions.
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy_s = '@#' + '#'.join(s) + '#!'  # '!' and '@' were used to avoid the index out of range.
        dummy_list = [0] * len(dummy_s)
        max_length = center = 0
        for i in range(1, len(dummy_s)-1):
            if i < max_length:
                dummy_list[i] = min(max_length - i, dummy_list[2 * center - i])
            while dummy_s[i - dummy_list[i] - 1] == dummy_s[i + dummy_list[i] + 1]:
                dummy_list[i] += 1
            if i + dummy_list[i] > max_length:
                center = i
                max_length = i + dummy_list[i]

        return sum((v+1)//2 for v in dummy_list)


if __name__ == '__main__':
    print(Solution().countSubstrings('aaa'))
    print(Solution().countSubstrings('a'))


#  Reading to Google 'Manacher's Algorithm'!

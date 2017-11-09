# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Write a function that takes a string as input and returns the string reversed.
# Example:
# Given s = "hello", return "olleh".

# 476 / 476 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 56.79 % of python submissions.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(reversed(s))


# TEL
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_ = ''
        for i in s:
            str_ = i + str_

        return str_


# 476 / 476 test cases passed.
# Status: Accepted
# Runtime: 49 ms
# Your runtime beats 37.51 % of python submissions.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == '__main__':
    print(Solution().reverseString('hello'))

# -*- encoding:utf-8 -*-
# __author__=='Gan'


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        dummy = x
        if x < 0:  # Negative isn't Palindrome.
            return False
        x = int(str(x)[::-1])
        return True if x == dummy else False

    # We should notice that one digit always is palindrome number.
    # And some special numbers like 10000, 1000.I usually transform them to the string.
    # For example, str(1000) will get 1. Obviously 1 is not equal 1000.

if __name__ == '__main__':
    print(Solution().isPalindrome(-2147447412))


# 11507 / 11507 test cases passed.
# Status: Accepted
# Runtime: 199 ms
# Your runtime beats 85.89 % of python submissions.

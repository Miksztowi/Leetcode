# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# 1. ord() can get ascii number.
# 2. subtract '0'.
# 3. z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')
# 4. remember the carry result.
# 315 / 315 test cases passed.
# Status: Accepted
# Runtime: 82 ms
# Your runtime beats 71.55 % of python3 submissions.
import itertools
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        z = itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0')
        zero2, carry, res = ord('0') * 2, 0, []
        for i in z:
            tmp = ord(i[0]) + ord(i[1]) + carry - zero2
            carry = tmp // 10
            res += str(tmp % 10),
        return ('1' if carry else '') + ''.join(res[::-1])

import itertools
from functools import reduce
# 315 / 315 test cases passed.
# Status: Accepted
# Runtime: 119 ms
# Your runtime beats 23.28 % of python3 submissions.
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(reduce(lambda a, b: a*10 + b,
                      map(lambda x: ord(x[0]) + ord(x[1]) - ord('0') * 2,
                          list(itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'))[::-1]
        )))

if __name__ == '__main__':
    print(Solution().addStrings(
        '98', '9'
    ))

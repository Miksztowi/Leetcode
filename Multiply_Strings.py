# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# 311 / 311 test cases passed.
# Status: Accepted
# Runtime: 449 ms
# Your runtime beats 31.28 % of python submissions.
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        for i, e1 in enumerate(num1[::-1]):
            for j, e2 in enumerate(num2[::-1]):
                res[i + j] += int(e1) * int(e2)
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return ''.join(map(str, res[::-1]))


if __name__ == '__main__':
    print(Solution().multiply('98', '8'))
    print(Solution().multiply('99', '9'))

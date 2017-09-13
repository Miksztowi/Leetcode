# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        max_length = max(len(a), len(b))
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        else:
            b = '0' * (len(a) - len(b)) + b
        l_a, l_b = list(a)[::-1], list(b)[::-1]
        result, carry, val = '', 0, 0
        for i in range(max_length):
            val = carry
            val += (int(l_a[i]) + int(l_b[i]))
            carry, val = val//2, val % 2
            result += str(val)
        if carry:
            result += str(carry)
        return result[::-1]

if __name__ == '__main__':
    print(Solution().addBinary('11','1'))


# 294 / 294 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 18.50 % of python submissions.



# Here is the geek solution!!!
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        x = int(a, 2)
        y = int(b, 2)

        t = bin(x + y)
        result = str(t)
        return result[2:]
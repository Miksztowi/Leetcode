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
        dummy = []
        for i in range(max_length):
            if l_a[i] != l_b[i]:
                dummy[i] = max(int(l_a[i]), int(l_b[i]))
            elif l_b[i] == 0:
                dummy[i] = '0'
            else:
                dummy[i] = '0'
                dummy[i+1] = '1'

        return ''.join(dummy)

if __name__ == '__main__':
    print(Solution().addBinary('11','1'))
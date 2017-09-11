# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
#
# click to show spoilers.
#
# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

class Solution(object):
    # This solution is mine.
    # Runtime: 59ms
    # Your runtime beats 27.54 % of python submissions.
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        dummpy = x
        if x < 0:
            negative = True
            dummpy = 0 - x
        s = str(dummpy)
        l = list(s)
        start = 0
        while start < len(l)//2:
            l[start], l[-(start+1)] = l[-(start+1)], l[start]
            start += 1
        if negative:
            l.insert(0, '-')
        res = int(''.join(l))
        if res > 2147483647 or res < -2147483648:
            return 0
        return res

# I think these solutions so cool.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x /= 10   # Here isn't suitable for python3.x, should use //=.
        return result if result <= 0x7fffffff else 0  # Handle overflow.

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
            x = int(str(x)[::-1])
        x = 0 if abs(x) > 0x7FFFFFFF else x
        return x
    #
    # def reverse3(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     s = cmp(x, 0)
    #     r = int(`s * x`[::-1])  # I still don't know that '`' means what.
    #     return s * r * (r < 2 ** 31)  # True is 1, and flase is 0.



if __name__ == '__main__':
    print(Solution().reverse(123))
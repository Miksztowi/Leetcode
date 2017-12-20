# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a positive integer n, find the number of non-negative integers less than or equal to n,
# whose binary representations do NOT contain consecutive ones.
# Example 1:
# Input: 5
# Output: 5
# Explanation:
# Here are the non-negative integers <= 5 with their corresponding binary representations:
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
# Note: 1 <= n <= 109

# Reference: http://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
# a[i]:the number of binatry string of length i which do not conatain any two consecutive 1s and end in 0
# b[i]:the number of binatry string of length i which do not conatain any two consecutive 1s and end in 1
# a[i]=a[i-1]+b[i-1]
# b[i]=a[i-1]
# 527 / 527 test cases passed.
# Status: Accepted
# Runtime: 62 ms
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = bin(num)[2:][::-1]
        l = len(binary)
        a = [0] * l
        b = [0] * l
        a[0] = b[0] = 1
        for i in range(1, l):
            a[i] = a[i - 1] + b[i - 1]
            b[i] = a[i - 1]

        result = a[l - 1] + b[l - 1]
        for i in range(l - 2, -1, -1):
            if binary[i + 1] == binary[i]:
                if binary[i] == '1':
                    break
                elif binary[i] == '0':
                    print(result, binary, b, i)
                    result -= b[i]
        return result


# Dp formula like above, but operation like Fibonacci.
# 527 / 527 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Your runtime beats 52.38 % of python submissions.
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        DP = [1, 2]
        binary = bin(num)[2:]
        l = len(binary)
        [DP.append(DP[-1] + DP[-2]) for _ in range(2, l + 1)]
        for i in range(1, l):
            if binary[i] == binary[i - 1]:
                if binary[i] == '1':
                    break
                if binary[i] == '0':
                    DP[-1] -= (DP[l - i] - DP[l - i - 1])
        return DP[-1]


if __name__ == '__main__':
    print(Solution().findIntegers(20))
    print(Solution().findIntegers(5))
    print(Solution().findIntegers(8))
    print(Solution().findIntegers(1))
    print(Solution().findIntegers(0))
    print(Solution().findIntegers(3))
    print(Solution().findIntegers(2))

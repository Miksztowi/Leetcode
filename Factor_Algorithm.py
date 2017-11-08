# -*- encoding:utf-8 -*-
# __author__=='Gan'

# 下面理清楚一些数学概念：
# 因数：一个数，如果存在可以被它整除的数，则这些数都是该数的因数。
# 规定0没有因数，1的因数是1，其他的比如4的因数有“1”、“2”、“4
# 因子：一个数，如果存在可以被它整除的数且这些数不包括它本身，则这些书都是该数的因子。
# 规定0没有因子，1的因子是1，其他的比如4的因子有“1”、“2”
# 质因子：一个数，如果可以分解成n个质数相乘，则n个质数成为该数的质因子。
# 规定0和1没有质因子，质数的质因子为其本身
# 完数：一个数的因子之和等于它本身，则该数为完数。


# 1. Given a non-negative number n, return all factors of it.
class Solution(object):
    def allFactor(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [1]
        if n == 1 or n == 2:
            return [n]

        for i in range(2, int(n ** 0.5)):
            if n % i == 0:
                ans += [i, n // i]

        return ans


# 2. Given a non-negative number n, return all common factors both of A and B.
# Solution:
# Using the Euclidean algorithm to get maximum common factor, then get all factor of it.
class Solution(object):
    def allCommonFactor(self, A, B):
        def gcd(a, b):  # Euclidean algorithm
            if b == 0:
                return a
            return gcd(b, a % b)

        maximum_common_factor = gcd(A, B)
        ans = {1}
        for i in range(2, maximum_common_factor + 1):
            if maximum_common_factor % i == 0:
                ans.add(i)
                ans.add(maximum_common_factor // i)

        return ans - {A} - {B}


if __name__ == '__main__':
    # print(Solution().allFactor(100))
    print(Solution().allCommonFactor(20, 8))
    print(Solution().allCommonFactor(30, 15))

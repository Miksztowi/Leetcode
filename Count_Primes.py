# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Description:
# Count the number of prime numbers less than a non-negative number, n.
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        up_bound = int((n ** 0.5) + 1)
        for i in range(2, up_bound):
            if primes[i]:
                # Starting from i * i. If i = 5, that 2 * 5, 3 * 5, 4 * 5 already done.
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])

        return sum(primes)


if __name__ == '__main__':
    print(Solution().countPrimes(3))

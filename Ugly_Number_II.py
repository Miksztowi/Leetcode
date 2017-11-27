# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Write a program to find the n-th ugly number.
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 596 / 596 test cases passed.
# Status: Accepted
# Runtime: 199 ms
# Your runtime beats 52.37 % of python submissions.
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return False
        ans = [1]
        factor2 = 0
        factor3 = 0
        factor5 = 0
        for i in range(1, n):
            ans += min(
                ans[factor2] * 2,
                ans[factor3] * 3,
                ans[factor5] * 5,
            ),
            if ans[-1] == ans[factor2] * 2:
                factor2 += 1
            if ans[-1] == ans[factor3] * 3:
                factor3 += 1
            if ans[-1] == ans[factor5] * 5:
                factor5 += 1
        return ans[-1]


# 596 / 596 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 97.52 % of python submissions.
class Solution(object):
    ans = sorted(
        (2 ** i) * (3 ** j) * (5 ** k)
        for i in range(32)
        for j in range(20)
        for k in range(14)
    )

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Use self, the instance only once iteration.
        return self.ans[n - 1]


# 596 / 596 test cases passed.
# Status: Accepted
# Runtime: 459 ms
# Your runtime beats 15.13 % of python submissions.
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                print(q2, q3, q5)
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(1))

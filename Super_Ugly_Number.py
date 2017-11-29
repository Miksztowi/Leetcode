# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Write a program to find the nth super ugly number.
# Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
# For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly
# numbers given primes = [2, 7, 13, 19] of size 4.
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# (4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# 83 / 83 test cases passed.
# Status: Accepted
# Runtime: 1035 ms
# Your runtime beats 41.02 % of python submissions.
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        if n <= 0:
            return 0
        ans = [1]
        primes_map = {p: 0 for p in primes}

        for i in range(1, n):
            ans += min([x * ans[primes_map[x]] for x in primes_map]),
            for i in primes:
                if ans[-1] == i * ans[primes_map[i]]:
                    primes_map[i] += 1
        return ans[n - 1]


# 83 / 83 test cases passed.
# Status: Accepted
# Runtime: 239 ms
# Your runtime beats 98.83 % of python submissions.
import heapq


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ans = [1] * n
        idx = [0] * n  # Handle the same value that in answer.
        p_index = [0] * len(primes)
        ugly_heap = []
        for i, k in enumerate(primes):
            heapq.heappush(ugly_heap, (k, i))

        for i in range(1, n):
            top, k = heapq.heappop(ugly_heap)
            ans[i] = top
            idx[i] = k
            p_index[k] += 1
            # When id[p_index[k]] > k that means the same value has been pushed to heap.
            # For example, when pushing 2 * 7 that 7 * 2 has been pushed, so skip this value.
            while idx[p_index[k]] > k:
                p_index[k] += 1
            heapq.heappush(ugly_heap, (primes[k] * ans[p_index[k]], k))
        return ans[-1]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(
        50, [2, 7, 13, 19]
    ))

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We are given an array A of positive integers, and two positive integers L and R (L <= R).
# Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element
# in that subarray is at least L and at most R.
# Example :
# Input:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# Output: 3
# Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
# Note:
# L, R  and A[i] will be an integer in the range [0, 10^9].
# The length of A will be in the range of [1, 50000].

# LeetCode Weekly Contest 74.
# 38 / 38 test cases passed.
# Status: Accepted
# Runtime: 48 ms

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        def count_subarrays(n):
            return n * (n + 1) // 2

        res, inc, exc = 0, 0, 0
        for num in A:
            if num > R:
                res += count_subarrays(inc) - count_subarrays(exc)
                inc = exc = 0
            elif num < L:
                inc += 1
                exc += 1
            else:
                inc += 1
                res -= count_subarrays(exc)
                exc = 0
        res += count_subarrays(inc) - count_subarrays(exc)
        return res


# LeetCode Weekly Contest 74.
# 38 / 38 test cases passed.
# Status: Accepted
# Runtime: 44 ms

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """

        def count(bound):
            res = 0
            tmp = 0
            for num in A:
                if num <= bound:
                    tmp += 1
                else:
                    tmp = 0
                res += tmp

            return res

        return count(R) - count(L - 1)


if __name__ == '__main__':
    print(Solution().numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
    print(Solution().numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))

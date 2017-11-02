# -*- encoding:utf-8 -*-
# __author__=='Gan'


# The set [1,2,3,…,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# Note: Given n will be between 1 and 9 inclusive.

# Solution: Like Digits_Count.
# perm_index = k // (m - 1)! and m is the length of current perm_elements. it's very important.
# target_str += perm_elements.pop(perm_index)
# k %= divide

# 200 / 200 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 83.66 % of python submissions.
from functools import reduce
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        perm_elements = [str(x) for x in range(1, n + 1)]
        target_str = ''
        k -= 1

        while k:
            divide = reduce(lambda x, y: x * y, range(1, len(perm_elements)))
            perm_index = k // divide
            target_str += perm_elements.pop(perm_index)
            k %= divide

        if perm_elements:
            target_str += ''.join(perm_elements)

        return target_str


if __name__ == '__main__':
    print(Solution().getPermutation(3, 1))

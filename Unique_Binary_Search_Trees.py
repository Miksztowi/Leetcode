# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# G(n) is number of unique BST for a sequence of length n.
# F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST,
# and the sequence ranges from 1 to n.
# G(n) = F(1, n) + F(2, n) + F(3, n) + ... + F(n, n)
# F(i, n) = G(i - 1) * G(n - i)
# G(n) = G(0) * G(n - 1) + G(1) + G(n - 2) + G(2) + G(n - 3) + ... + G(n - 1) * G(n)
# 19 / 19 test cases passed.
# Status: Accepted
# Runtime: 29 ms
# Your runtime beats 81.28 % of python submissions.
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        combine_list = [0] * (n + 1)
        combine_list[0] = combine_list[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                combine_list[i] += combine_list[j-1] * combine_list[i-j]
        return combine_list[1]


# Catalan number!
# 19 / 19 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 39.76 % of python submissions.
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import reduce
        mul = lambda x, y: x * y
        # reduce(mul, iterator, 1) to handle the 0.
        # Otherwise TypeError: reduce() of empty sequence with no initial value.
        return reduce(mul, range(n + 1, (2 * n) + 1), 1) // (reduce(mul, range(1, n + 1), 1) * (n+1))


if __name__ == '__main__':
    print(Solution().numTrees(0))
    print(Solution().numTrees(3))
    print(Solution().numTrees(4))
    print(Solution().numTrees(5))

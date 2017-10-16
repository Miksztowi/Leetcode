# -*- encoding:utf-8 -*-
# __author__=='Gan'


# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given two integers x and y, calculate the Hamming distance.
# Note:
# 0 ≤ x, y < 231.
# Example:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


if __name__ == '__main__':
    print(Solution().hammingDistance(1, 4))
    print(Solution().hammingDistance(3, 1))
    print(Solution().hammingDistance(4, 2))


# 149 / 149 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Your runtime beats 77.81 % of python submissions.

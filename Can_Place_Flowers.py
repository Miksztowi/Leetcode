# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Suppose you have a long flowerbed in which some of the plots are planted and some are not.
# However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
# and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# Example 1:
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Example 2:
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# Note:
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.


# 123 / 123 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Your runtime beats 67.58 % of python submissions.
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        lo, hi = 0, len(flowerbed)
        while lo < hi:
            if (lo == 0 or not flowerbed[lo - 1]) and not flowerbed[lo] and (lo == hi - 1 or not flowerbed[lo + 1]):
                flowerbed[lo] = 1
                n -= 1
            lo += 1
        print(flowerbed)
        return n <= 0


if __name__ == '__main__':
    # print(Solution().canPlaceFlowers([1, 0, 0, 0, 1], 1))
    # print(Solution().canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
    # print(Solution().canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))
    print(Solution().canPlaceFlowers([0, 0, 1, 0, 0], 1))
    # print(Solution().canPlaceFlowers([0,1, 0], 1))

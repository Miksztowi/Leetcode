# -*- encoding:utf-8 -*-
# __author__=='Gan'

# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
# Given a starting point (sx, sy) and a target point (tx, ty),
# return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty).
# Otherwise, return False.
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True

# 189 / 189 test cases passed.
# Status: Accepted
# Runtime: 59 ms
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while sx <= tx and sy <= ty:
            if tx > ty:
                if sy == ty and (tx - sx) % ty == 0:
                    return True
                tx %= ty
            else:
                if sx == tx and (ty - sy) % tx == 0:
                    return True
                ty %= tx
        return False



if __name__ == '__main__':
    print(Solution().reachingPoints(35, 13, 455955547, 546465461))
    print(Solution().reachingPoints(1, 1, 10, 1))
    print(Solution().reachingPoints(1, 1, 3, 5))
    print(Solution().reachingPoints(1, 1, 2, 2))

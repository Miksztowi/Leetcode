# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# For example,
# Consider the following matrix:
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (matrix and matrix[0]):
            return False

        for row in matrix:
            if target > row[-1]:
                continue
            lo, hi = 0, len(row)
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False







if __name__ == '__main__':
    print(Solution().searchMatrix(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ], 3
    ))
    print(Solution().searchMatrix([[]], 1))
    print(Solution().searchMatrix([[1]], 2))
    print(Solution().searchMatrix([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0))


# 136 / 136 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 87.01 % of python submissions.


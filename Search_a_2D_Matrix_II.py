# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# For example,
# Consider the following matrix:
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (matrix and matrix[0]):
            return False

        for row in range(len(matrix)):
            if matrix[row][-1] < target:
                continue
            for col in range(len(matrix[row])-1, -1, -1):
                if matrix[row][col] > target:
                    continue
                elif matrix[row][col] == target:
                    return True
                lo, hi = row, len(matrix)
                while lo < hi:
                    mid = (lo + hi) // 2
                    if matrix[mid][col] == target:
                        return True
                    elif matrix[mid][col] > target:
                        hi = mid - 1
                    else:
                        lo = mid + 1
        return False

# 129 / 129 test cases passed.
# Status: Accepted
# Runtime: 102 ms
# Your runtime beats 44.52 % of python submissions.


# This solution is simpler and faster than the above.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not (matrix and matrix[0]):
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


# 129 / 129 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 59.57 % of python submissions.



if __name__ == '__main__':
    print(Solution().searchMatrix(
        [
          [1,   4,  7, 11, 15],
          [2,   5,  8, 12, 19],
          [3,   6,  9, 16, 22],
          [10, 13, 14, 17, 24],
          [18, 21, 23, 26, 30]
        ], 31
    ))

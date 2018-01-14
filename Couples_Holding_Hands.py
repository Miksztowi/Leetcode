# -*- encoding:utf-8 -*-
# __author__=='Gan'

# N couples sit in 2N seats arranged in a row and want to hold hands.
# We want to know the minimum number of swaps so that every couple is sitting side by side.
# A swap consists of choosing any two people, then they stand up and switch seats.
# The people and seats are represented by an integer from 0 to 2N-1,
# the couples are numbered in order, the first couple being (0, 1),
# the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).
# The couples' initial seating is given by row[i] being the value of the person
# who is initially sitting in the i-th seat.
# Example 1:
# Input: row = [0, 2, 1, 3]
# Output: 1
# Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
# Example 2:
# Input: row = [3, 2, 0, 1]
# Output: 0
# Explanation: All couples are already seated side by side.
# Note:
# len(row) is even and in the range of [4, 60].
# row is guaranteed to be a permutation of 0...len(row)-1.

# Leetcode Weekly Contest 67.
# 56 / 56 test cases passed.
# Status: Accepted
# Runtime: 36 ms
# Scan from left to right, if non-couple sitting in 2 seat block, swap row[i-1] with the spouse one which in row[i:].
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        row = [c // 2 for c in row]
        count = 0
        for i in range(0, len(row) - 1, 2):
            if row[i] != row[i + 1]:
                p = row.index(row[i], i + 1)
                row[p] = row[i + 1]
                row[i + 1] = row[i]
                count += 1
        return count


# 56 / 56 test cases passed.
# Status: Accepted
# Runtime: 38 ms
class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        hash_row = {x: i for i, x in enumerate(row)}
        count = 0
        for i in range(0, len(row) - 1, 2):
            if row[i] % 2 == 0:
                spouse_one = row[i] + 1
            else:
                spouse_one = row[i] - 1
            j = hash_row[spouse_one]

            if abs(i - j) > 1:
                row[i + 1], row[j] = row[j], row[i + 1]
                hash_row[row[i + 1]] = i + 1
                hash_row[row[j]] = j
                count += 1
        return count


if __name__ == '__main__':
    print(Solution().minSwapsCouples([0, 2, 1, 3]))

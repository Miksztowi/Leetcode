# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.
# The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].
# The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].
# Return true if and only if the number of global inversions is equal to the number of local inversions.
# Example 1:
# Input: A = [1,0,2]
# Output: true
# Explanation: There is 1 global inversion, and 1 local inversion.
# Example 2:
# Input: A = [1,2,0]
# Output: false
# Explanation: There are 2 global inversions, and 1 local inversion.
# Note:
# A will be a permutation of [0, 1, ..., A.length - 1].
# A will have length in range [1, 5000].
# The time limit for this problem has been reduced.

# Leetcode Weekly Contest 69.
# 208 / 208 test cases passed.
# Status: Accepted
# Runtime: 125 ms
class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        pre_max = float('-inf')
        for i in range(len(A) - 2):
            pre_max = max(pre_max, A[i])
            if pre_max > A[i + 2]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isIdealPermutation([1, 0, 2]))
    print(Solution().isIdealPermutation([1, 2, 0]))
    print(Solution().isIdealPermutation([2, 0, 1]))

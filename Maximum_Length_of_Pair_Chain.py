# -*- encoding:utf-8 -*-
# __author__=='Gan'

# You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
# Chain of pairs can be formed in this fashion.
# Given a set of pairs, find the length longest chain which can be formed.
# You needn't use up all the given pairs. You can select pairs in any order.
# Example 1:
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# Note:
# The number of given pairs will be in the range [1, 1000].


# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 84 ms
# Your runtime beats 51.01 % of python submissions.
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs) <= 1:
            return len(pairs)
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        max_length = 1
        cur_node = sorted_pairs[0][1]
        for p in sorted_pairs[1:]:
            if cur_node < p[0]:
                max_length += 1
                cur_node = p[1]
        return max_length


if __name__ == '__main__':
    # print(Solution().findLongestChain([[1, 2], [2, 3], [3, 4]]))
    print(Solution().findLongestChain([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]))
    # print(Solution().findLongestChain([[1, 2]]))

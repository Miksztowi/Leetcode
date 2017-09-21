# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            dummy = []
            for perm in res:
                for i in range(len(perm)+1):
                    dummy.append(perm[:i] + [num] + perm[i:])
            res = dummy
        return res


if __name__ == '__main__':
    print(Solution().permute([x for x in range(3)]))

# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 75 ms
# Your runtime beats 34.78 % of python submissions.


#  What?!!!
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        l = list(permutations(nums))

        return l

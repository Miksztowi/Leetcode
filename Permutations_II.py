# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 195 ms
# Your runtime beats 6.97 % of python submissions.
from collections import Counter
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def permute(count, path, length):
            if len(path) == length:
                self.result += path,

            for i in count:
                if count[i]:
                    count[i] -= 1
                    permute(count, path + [i], length)
                    count[i] += 1

        self.result = []

        permute(Counter(nums), [], len(nums))
        return self.result


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 88 ms
# Your runtime beats 99.45 % of python submissions.
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for num in nums:
            dummy = []
            for perm in ans:
                for i in range(len(perm)+ 1):
                    dummy.append(perm[:i] + [num] + perm[i:])
                    if i < len(perm) and perm[i] == num:  # Handle the Duplicate number.
                        break
            ans = dummy

        return ans


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 1, 2]))
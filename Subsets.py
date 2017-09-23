# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a set of distinct integers, nums, return all possible subsets.
# Note: The solution set must not contain duplicate subsets.
# For example,
# If nums = [1,2,3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            dummy = []
            for r in res:
                dummy.append(r+[num])
                print(dummy, num)
            res += dummy
        return res

# Concise
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [item+[num] for item in res]
        return res


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))


# 10 / 10 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 83.71 % of python submissions.


# Below are from leetcode.

# DFS recursively
def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, i + 1, path + [nums[i]], res)


# Bit Manipulation
def subsets2(self, nums):
    res = []
    nums.sort()
    for i in range(1 << len(nums)):  # To generate 000, 001, 010, 011, 100, 101, 110, 111.
        tmp = []
        for j in range(len(nums)):
            if i & 1 << j:  # if i >> j & 1:
                #  To generate [], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]
                tmp.append(nums[j])
        res.append(tmp)
    return res


# Iteratively
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item + [num] for item in res]
    return res

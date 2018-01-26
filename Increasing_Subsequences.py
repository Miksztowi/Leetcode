# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an integer array, your task is to find all the different possible increasing subsequences of the given array,
# and the length of an increasing subsequence should be at least 2 .
# Example:
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# Note:
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered
# as a special case of increasing sequence.

# TEL!
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = list()

        def dfs(idx, path):
            if idx > len(nums):
                return
            for i in range(idx, len(nums)):
                tmp = path + [nums[i]]
                if len(tmp) > 1 and tmp not in ans and nums[i] >= path[-1]:
                    ans.append(tmp)
                dfs(i + 1, tmp)
        dfs(0, [])
        return ans


# 57 / 57 test cases passed.
# Status: Accepted
# Runtime: 752 ms
# Your runtime beats 51.46 % of python submissions.
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = {()}
        for num in nums:
            subs.update({
                sub + (num,)
                for sub in subs
                if not sub or sub[-1] <= num
            })
        return [sub for sub in subs if len(sub) > 1]


# 57 / 57 test cases passed.
# Status: Accepted
# Runtime: 1257 ms
# Your runtime beats 2.43 % of python submissions.
import itertools
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [x
                for i in range(2, len(nums) + 1)
                for x in set(itertools.combinations(nums, i))
                if all(a <= b for a, b in zip(x, x[1:]))]


if __name__ == '__main__':
    print(Solution().findSubsequences([4, 6, 7, 7]))
    print(Solution().findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

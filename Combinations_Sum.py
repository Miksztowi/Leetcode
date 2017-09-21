# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]

# Don't need to sort, but it's too slow.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        def helper(index, candidates, target, combination=[]):
            for i in range(index, len(candidates)):
                if target < 0:
                    return
                if target == 0:
                    return combinations.append(combination)
                else:
                    helper(i, candidates, target - candidates[i],  combination+[candidates[i]])
        helper(0, candidates, target)
        return combinations



class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target:
            return []

        def helper(index, candidates, target, combination=[]):
                if target == 0:
                    return combinations.append(combination)
                for i in range(index, len(candidates)):
                    if candidates[i] > target:
                        break
                    # combination.append(candidates[i])
                    # In[44]: timeit('x += [1]', 'x = []', number=1000000)
                    # Out[44]: 0.21148269201512448
                    # In[45]: timeit('x.append(1)', 'x = []', number=1000000)
                    # Out[45]: 0.1697585310030263
                    # In[52]: timeit('x += 1,', 'x = []', number=1000000)  # += 1,
                    # Out[52]: 0.12951252100174315
                    # So, use [].append() will be faster.
                    helper(i, candidates, target - candidates[i],  combination + [candidates[i]])

        combinations = []
        candidates.sort()
        helper(0, candidates, target)

        return combinations


if __name__ == '__main__':
    print(Solution().combinationSum([5, 2, 3, 6, 7], 7))
    print(Solution().combinationSum([], 7))
    print(Solution().combinationSum([], ''))


# 168 / 168 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 79.71 % of python submissions.


# Here is the fastest solution in Leetcode. runtime: 68ms.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target:
            return []
        candidates.sort()
        self.res = []
        self.dfs(candidates, 0, target, [])
        return self.res

    def dfs(self, candidates, start, remain_target, ans):
        if remain_target == 0:
            self.res.append(ans[:]) # Don't append(ans)!
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remain_target:
                break
            ans.append(candidates[i])
            self.dfs(candidates, i, remain_target - candidates[i], ans)
            del ans[-1] # Avoid to copy the list,  but the faster way is ans += candidates,

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# You are given a list of non-negative integers, a1, a2, ..., an,
# and a target, S. Now you have 2 symbols + and -. For each integer,
# you should choose one from + and - as its new symbol.
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# There are 5 ways to assign symbols to make the sum of nums be target 3.

# TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def search(index, cur_sum, res = 0):
            if index == len(nums):
                if S == cur_sum:
                    res += 1
                return res

            return search(index + 1, cur_sum + nums[index]) + search(index + 1, cur_sum - nums[index])

        res = search(0, 0)

        return res


# 139 / 139 test cases passed.
# Status: Accepted
# Runtime: 118 ms
# Your runtime beats 84.89 % of python submissions.
import collections
# This solution can also replace defaultdict with list.
# res_list = [0] * (target + 1)
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_ = sum(nums)
        if sum_ < S or (sum_ + S) % 2:
            return 0
        target = (sum_ + S) // 2
        res_dic = collections.defaultdict(int)
        res_dic[0] = 1
        for num in nums:
            for i in range(target, num - 1, -1):
                if i - num in res_dic:
                    res_dic[i] += res_dic[i-num]
        return res_dic[target]



# 139 / 139 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Your runtime beats 99.75 % of python submissions.
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_ = sum(nums)
        if sum_ < S or (sum_ + S) % 2:
            return 0
        target = (sum_ - S) // 2
        res_list = [0] * (target + 1)
        res_list[0] = 1
        for num in nums:
            for i in range(target, num-1, -1):
                # if i - num  in res_list:  Do not need to judge.
                res_list[i] += res_list[i - num]
        return res_list[target]


# 139 / 139 test cases passed.
# Status: Accepted
# Runtime: 316 ms
# Your runtime beats 58.47 % of python submissions.
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sum_ = sum(nums)
        if sum_ < S or (sum_ + S) % 2:
            return 0
        res_dict = {nums[0]: 1, -nums[0]: 1} if nums[0] else {0:2}
        for num in nums[1:]:
            dummy_dict = {}
            for d in res_dict:
                    dummy_dict[d-num] = dummy_dict.get(d-num, 0) + res_dict.get(d, 0)
                    dummy_dict[d+num] = dummy_dict.get(d+num, 0) + res_dict.get(d, 0)
            res_dict = dummy_dict
        return res_dict[S]





if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    print(Solution().findTargetSumWays([1,2,7,9,981], 1000000000))

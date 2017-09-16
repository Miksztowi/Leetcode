# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.
# Note: The solution set must not contain duplicate triplets.
# For example, given array S = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Here it's my first solution.It's failed.
# I think if a + b < 0 that should abandon the b.And judge  a + (b-1) if still less 0.
# For example, b = -5, a = 4 and then abandon the b.If nums have 1,then find the answer.
# But if the nums still have 3 and 2, they also right. [-5, 4, 1] and [-5, 3, 2].
# So -5 is can't be abandoned.
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         left, right = 0, len(nums) - 1
#         transition_dict = {}
#         dummy_list = []
#         res__list_list = []
#
#         nums.sort()
#         for num in nums:
#             if transition_dict.get(num):
#                 transition_dict[num] += 1
#             else:
#                 transition_dict[num] = 1
#         print(transition_dict)
#         while left < right:
#             if (max(nums[right], nums[left]) < 0) or (min(nums[right], nums[left]) > 0):
#                 break
#             dummy = 0 - (nums[left] + nums[right])
#             if transition_dict.get(dummy):
#                 dummy_list.append([dummy, nums[left], nums[right]])
#
#             if nums[left] + nums[right] < 0:
#                 left += 1
#             else:
#                 right -= 1
#
#         print(dummy_list)
#         for i in range(len(dummy_list) - 1):
#             res__list_list.append(dummy_list[i])
#             for res__list in dummy_list[i]:
#                 if transition_dict[res__list] < dummy_list.count(res__list):
#                     res__list_list.pop()
#                     break
#         return res__list_list

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # i > 0 guarantee that len(nums) > 3.Can handle [0, 0, 0].
                continue  # Avoid to handle the same value.Because if value is same, it will get the same groups too.
            left, right = i + 1, len(nums) - 1
            while left < right:
                dummy = nums[i] + nums[left] + nums[right]
                if dummy < 0:
                    left += 1
                elif dummy > 0:
                    right -= 1
                else:
                    res_list.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # avoid to handle the same group.
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res_list


if __name__ == '__main__':
    print(Solution().threeSum([1,2,-1,-1]))
    print(Solution().threeSum([-1,0,1,2,-1,-4]))

# 313 / 313 test cases passed.
# Status: Accepted
# Runtime: 972 ms
# Your runtime beats 76.59 % of python submissions.


# Here is the fastest solution in leetcode.
class Solution(object):
    def threeSum(self, nums):
        result, counter = [], {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        uniques = counter.keys()
        positives = [num for num in uniques if num >= 0]
        negatives = [num for num in uniques if num < 0]

        if 0 in counter and counter[0] > 2:
            result.append([0, 0, 0])

        for p in positives:
            for n in negatives:
                inverse = -(p + n)
                if inverse in counter:
                    if (inverse == p or inverse == n) and counter[inverse] > 1:
                        result.append([p, n, inverse])
                    elif inverse > p or inverse < n:
                        result.append([p, n, inverse])
        return result


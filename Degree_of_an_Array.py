# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty array of non-negative integers nums,
# the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of
#  a (contiguous) subarray of nums, that has the same degree as nums.
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation:
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6


import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        counter = collections.Counter(nums)
        max_time = counter[max(counter, key=lambda x: counter[x])]
        dummy = []
        for i in counter:
            if counter[i] == max_time:
                dummy.append(i)
        res_lambda = lambda max_time: (len(nums) - 1 - nums[::-1].index(max_time)) - nums.index(max_time) + 1
        res_list = map(res_lambda, dummy)
        return min(res_list)


# Other contestants's solution.
class Solution(object):
    def findShortestSubArray(self, nums):
        first_pos = {}
        last_pos = {}
        count = collections.Counter(nums)
        for i in range(len(nums)):
            first_pos.setdefault(nums[i], i)  # equal if nums[i] not in first_pos then do ....
            last_pos[nums[i]] = i
        max_times = max(count.values())
        return min([last_pos[p] - first_pos[p] + 1 for p in count if count[p] == max_times])


class Solution(object):
    def findShortestSubArray(self, nums):
        position_dict, degree, min_length = collections.defaultdict(list), 0, float('inf')
        for i, num in enumerate(nums):
            position_dict[num].append(i)
            if degree == len(position_dict[num]):
                min_length = min(min_length, position_dict[num][-1] - position_dict[num][0] + 1)
            elif degree < len(position_dict[num]):
                degree = len(position_dict[num])
                min_length = position_dict[num][-1] - position_dict[num][0] + 1
        return min_length



if __name__ == '__main__':
    print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))
    print(Solution().findShortestSubArray([1,2,2,3,1]))
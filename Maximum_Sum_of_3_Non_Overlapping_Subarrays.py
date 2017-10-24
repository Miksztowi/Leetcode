# -*- encoding:utf-8 -*-
# __author__=='Gan'

# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
# Return the result as a list of indices representing the starting position of each interval (0-indexed).
# If there are multiple answers, return the lexicographically smallest one.
# Example:
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
# Note:
# nums.length will be between 1 and 20000.
# nums[i] will be between 1 and 65535.
# k will be between 1 and floor(nums.length / 3).

# https://discuss.leetcode.com/topic/105577/c-java-dp-with-explanation-o-n
# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 159 ms
# Your runtime beats 31.18 % of python submissions.
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        sum_list = [0]
        length = len(nums)
        pos_left_memo, pos_right_memo = [0] * length, [0] * length
        max_combination = float('-inf')
        ans = [0, 0, 0]
        for i in range(length):
            sum_list.append(sum_list[i] + nums[i])

        tot = sum_list[k] - sum_list[0]
        for i in range(k, length):
            if sum_list[i+1] - sum_list[i+1-k] > tot:
                tot = sum_list[i+1] - sum_list[i+1-k]
                pos_left_memo[i] = i+1-k
            else:
                pos_left_memo[i] = pos_left_memo[i-1]

        pos_right_memo[length-k] = length - k
        tot = sum_list[length] - sum_list[length-k]
        for i in range(length-k-1, -1, -1):
            if sum_list[i+k] - sum_list[i] >= tot:
                pos_right_memo[i] = i
                tot = sum_list[i+k] - sum_list[i]
            else:
                pos_right_memo[i] = pos_right_memo[i+1]

        for i in range(k, length - 2*k +1):
            l, r = pos_left_memo[i-1], pos_right_memo[i+k]
            tot = sum_list[i+k] - sum_list[i] + sum_list[l+k] - sum_list[l] + sum_list[r+k] - sum_list[r]
            if tot > max_combination:
                max_combination = tot
                ans = [l, i, r]
        print(pos_left_memo, pos_right_memo)
        return ans


# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 78 ms
# Your runtime beats 98.80 % of python submissions.
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        size = len(nums) - k + 1
        subs = [0]*size
        subs[0] = sum(nums[:k])
        value = [0, 0, 0]
        index = [
            [0],
            [0, 0],
            [0, 0, 0]
        ]
        for i in range(size - 1):
            subs[i + 1] = subs[i] - nums[i] + nums[i + k]
        for i in range(size - 2 * k):
            a, b, c = subs[i], subs[i + k], subs[i + 2 * k]
            if a > value[0]:
                value[0] = a
                index[0] = [i]
            if b + value[0] > value[1]:
                value[1] = b + value[0]
                index[1] = index[0] + [i + k]
            if c + value[1] > value[2]:
                value[2] = c + value[1]
                index[2] = index[1] + [i + 2 * k]
                result = index[2]

        return result


if __name__ == '__main__':
    print(Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2))
    print(Solution().maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3))

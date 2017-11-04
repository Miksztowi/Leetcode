# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
# Your algorithm should run in O(n) complexity.


# Hash Map
# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 46.91 % of python submissions.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        hash_map = {}
        max_length = 0
        for num in nums:
            if not hash_map.get(num):  # handle duplicate number
                left = hash_map.get(num - 1, 0)
                right = hash_map.get(num + 1, 0)
                hash_map[num] = left + right + 1
                max_length = max(max_length, left + right + 1)

                hash_map[num - left] = left + right + 1  # Update the boundary value.
                hash_map[num + right] = left + right + 1  # Update the boundary value.

        return max_length


# 68 / 68 test cases passed.
# Status: Accepted
# Runtime: 45 ms
# Your runtime beats 46.91 % of python submissions.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in nums:
                next_num = num + 1
                while next_num in nums:
                    next_num += 1
                max_length = max(max_length, next_num - num)

        return max_length


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([1, 2, 0, 1]))
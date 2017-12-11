# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You are given an integer array sorted in ascending order (may contain duplicates),
# you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers.
# Return whether you can make such a split.
# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3
# 3, 4, 5
# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences :
# 1, 2, 3, 4, 5
# 3, 4, 5
# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False
# Note:
# The length of the input is in range of [1, 10000]


# We iterate through the array once to get the frequency of all the elements in the array
# We iterate through the array once more and for each element we either see if it can be appended to a previously
# constructed consecutive sequence or if it can be the start of a new consecutive sequence. If neither are true,
# then we return false.
# 180 / 180 test cases passed.
# Status: Accepted
# Runtime: 279 ms
# Your runtime beats 38.06 % of python submissions.
import collections
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq_map = collections.Counter(nums)
        append_fre = {}
        for num in nums:
            if freq_map.get(num, 0) == 0:
                continue
            elif append_fre.get(num, 0) > 0:
                append_fre[num] -= 1
                append_fre[num + 1] = append_fre.get(num + 1, 0) + 1
            elif freq_map.get(num + 1, 0) > 0 and freq_map.get(num + 2, 0) > 0:
                freq_map[num + 1] -= 1
                freq_map[num + 2] -= 1
                append_fre[num + 3] = append_fre.get(num + 3, 0) + 1
            else:
                return False
            freq_map[num] -= 1

        return True

if __name__ == '__main__':
    print(Solution().isPossible([1,2,3,3,4,4,5,5]))
    print(Solution().isPossible([1,2,3,3,4,4,5]))
# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty array of integers, return the third maximum number in this array.
# If it does not exist, return the maximum number. The time complexity must be in O(n).
# Example 1:
# Input: [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]
# Output: 1
# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.



# 26 / 26 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 27.53 % of python submissions.
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        values = [float('-inf')] * 3
        for num in nums:
            if num not in values:
                if num > values[0]:
                    values = [num, values[0], values[1]]
                elif num > values[1]:
                    values = [values[0], num, values[1]]
                elif num > values[2]:
                    values[2] = num
        return max(nums) if float('-inf') in values else values[2]


if __name__ == '__main__':
    assert Solution().thirdMax([1, 2, 3]) == 1
    assert Solution().thirdMax([1, 2, 2]) == 2
    assert Solution().thirdMax([1, 2]) == 2

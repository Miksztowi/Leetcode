# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has,
# please find out a way you can make one square by using up all those matchsticks. You should not break any stick,
# but you can link them up, and each matchstick must be used exactly one time.
# Your input will be several matchsticks the girl has, represented with their stick length.
# Your output will either be true or false, to represent whether you could make one square using all the
# matchsticks the little match girl has.
# Example 1:
# Input: [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
# Example 2:
# Input: [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the matchsticks.
# Note:
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.


# 174 / 174 test cases passed.
# Status: Accepted
# Runtime: 2419 ms
# Your runtime beats 13.39 % of python submissions.
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        side_sum = sum(nums)
        side = side_sum // 4
        if len(nums) < 4 or side_sum % 4:
            return False
        nums.sort(reverse=True)
        square_side = [side] * 4
        print(side_sum, side)

        def dfs(idx, square_side):
            if idx == len(nums):
                return True
            for i in range(4):
                if square_side[i] >= nums[idx]:
                    square_side[i] -= nums[idx]
                    if dfs(idx + 1, square_side):
                        return True
                    square_side[i] += nums[idx]
            return False

        return dfs(0, square_side)


# 174 / 174 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 96.85 % of python submissions.
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def backtracking(i, tot):
            if tot == 0:
                return True
            if i == len(nums):
                return False
            if 0 < num[i] <= tot:
                num[i] = -num[i]
                if backtracking(i + 1, tot + num[i]):
                    return True
                num[i] = -num[i]
            return backtracking(i + 1, tot)

        if len(nums) < 4:
            return False

        if sum(nums) % 4 != 0:
            return False

        num = sorted(nums, reverse=True)

        for i in range(4):
            if not backtracking(0, sum(nums) / 4):
                return False

        return True


if __name__ == '__main__':
    # print(Solution().makesquare([1, 1, 2, 2, 2]))
    # print(Solution().makesquare([2, 2, 2, 2, 2, 6]))
    # print(Solution().makesquare([3, 3, 3, 3, 4]))
    print(Solution().makesquare(
        [5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540, 2324577, 6810719, 8936380, 7868365, 2755770,
         9954463, 9912280, 4713511]))

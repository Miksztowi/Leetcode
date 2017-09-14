# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# Here is my solution, but it is too slowly to get pass.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        res = max(nums)
        for i in range(len(nums)):
            sum_ = nums[i]
            for j in range(i+1, len(nums)):
                sum_ += nums[j]
                if sum_ < 0:
                    break
                res = max(sum_, res)
        return res


# Here is cool solution.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum, max_sum = nums[0], nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(cur_sum, max_sum)

# 202 / 202 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 41.14 % of python submissions.


if __name__ == '__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(Solution().maxSubArray([1,2]))
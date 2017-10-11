# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right.
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Therefore, return the max sliding window as [3,3,5,5,6,7].


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        maxs = []
        start = 0
        while k <= len(nums):
            maxs.append(max(nums[start:k]))
            k += 1
            start += 1
        return maxs

# solution: Avoid to use 'max()' when cur_max is not equal the num[i].
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        cur_max = max(nums[:k])
        maxs = [cur_max]
        for i in range(len(nums)-k):
            if nums[i] == cur_max:
                cur_max = max(nums[i+1:k+i+1])
            elif nums[i+k] > cur_max:
                cur_max = nums[i+k]
            maxs.append(cur_max)
        return maxs


if __name__ == '__main__':
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


# 18 / 18 test cases passed.
# Status: Accepted
# Runtime: 159 ms
# Your runtime beats 99.39 % of python submissions.

# Here is the Geek Solution!
# Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing,
# and their corresponding nums are decreasing. Then the first deque element is the index of the largest window value.
# For each index i:
# Pop (from the end) indexes of smaller elements (they'll be useless).
# Append the current index.
# Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
# If our window has reached size k, append the current window maximum to the output.

import collections


def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out



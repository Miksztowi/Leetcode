# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        dummy, max_Area, left, right = 0, 0, 0, len(height) - 1
        while left < right:
            dummy = (right - left) * min(height[left], height[right])
            max_Area = max(max_Area, dummy)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return max_Area


if __name__ == '__main__':
    print(Solution().maxArea([1,1]))

# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 69 ms
# Your runtime beats 67.62 % of python submissions.



# Here is the fastest solution.But this solution is O(n) too.
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        small = 0
        big = len(height) - 1
        w = big - small
        if height[big] > height[small]:
            h = height[small]
            small += 1
        else:
            h = height[big]
            big -= 1
        area = w * h
        while small < big:
            w = big - small
            if height[big] > height[small]:

                h = height[small]
                small += 1
            else:

                h = height[big]
                big -= 1
            new_area = w * h
            if new_area > area:
                area = new_area
        return area


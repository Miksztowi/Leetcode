# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo, hi = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_stored = 0

        while lo < hi:
            left_max = max(height[lo], left_max)
            right_max = max(height[hi], right_max)
            if left_max < right_max:
                water_stored += left_max - height[lo]
                lo += 1
            else:
                water_stored += right_max - height[hi]
                hi -= 1

        return water_stored

if __name__ == '__main__':
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(Solution().trap([]))
    # print(Solution().trap([0,1,1]))

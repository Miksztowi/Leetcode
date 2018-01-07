# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We are given a list avail of employees, which represents the free time for each employee.
# Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
# Return the list of finite intervals representing common, positive-length free time for all employees,
# also in sorted order.
# Example 1:
# Input: avails = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# Output: [[3,4]]
# Explanation:
# There are a total of three employees, and all common
# free time intervals would be [-inf, 1], [3, 4], [10, inf].
# We discard any intervals that contain inf as they aren't finite.
# Example 2:
# Input: avails = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# Output: [[5,6],[7,9]]
# (Even though we are representing Intervals in the form [x, y], the objects inside are Intervals,
# not lists or arrays. For example, avails[0][0].start = 1, avails[0][0].end = 2, and avails[0][0][0] is not defined.)
# Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
# Note:
# avails and avails[i] are lists with lengths in range [1, 50].
# 0 <= avails[i].start < avails[i].end <= 10^8.


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# Leetcode weekly contest 66.
# The solution is to sort all the intervals on the starting time. This gives a set of busy intervals. After merging
# all busy times, the gaps in between, form the free time common to everyone in the list.
# Using a stack, we can start merging the intervals, and whenever a new interval is pushed the stack, the time between
# the last seen interval and the new interval is a free time that can be added to the result.
# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 198 ms
class Solution(object):
    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        if not avails:
            return []
        avails_map = []
        for person in avails:
            for a in person:
                avails_map += [a.start, a.end],
        avails_map.sort(key=lambda x: x[0])
        ans = []
        left, right = avails_map[0][0], avails_map[0][1]
        for i in range(len(avails_map)):
            if right < avails_map[i][0]:
                ans.append([left, right])
                left = avails_map[i][0]
                right = avails_map[i][1]
            else:
                if right < avails_map[i][1]:
                    right = avails_map[i][1]
        ans.append([left, right])
        res = []
        for i in range(len(ans) - 1):
            res.append([ans[i][1], ans[i + 1][0]])
        return res


# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 210 ms
from functools import reduce
class Solution(object):
    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        avails = sorted(reduce(lambda x, y: x + y, avails, []), key=lambda x: x.start)
        stack = [avails[0]]
        ans = []
        for cur in avails[1:]:
            top = stack.pop()
            if top.end < cur.start:
                ans.append([top.end, cur.start])
                stack.append(cur)
            else:
                if top.end > cur.end:
                    stack.append(top)
                else:
                    stack.append(cur)
        return ans


if __name__ == '__main__':
    a = [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]]
    print(Solution().employeeFreeTime(a))
    # print(Solution().employeeFreeTime([]))

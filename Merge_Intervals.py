# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a collection of intervals, merge all overlapping intervals.
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# [1,4] [5,6] have no intersection, but this way will get one, so it's failed.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        dummy = [False] * 1000  # Ugly way.
        for i in intervals:
            dummy[i.start:i.end+1] = [True] * (i.end - i.start + 1)
        # print(dummy)
        left = None
        res = []
        for i, d in enumerate(dummy):
            if not left and d:
                left = i
            if not d and left:
                res.append([left, i-1])
                left = None
        return res


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 1:
            return []
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]
        for i in intervals:
            if res[-1].end >= i.start:
                res[-1].end = max(res[-1].end, i.end)
            else:
                res += i,
        return res



if __name__ == '__main__':
    # print(Solution().merge((Interval(1,3), Interval(2, 6), Interval(8, 10), Interval(15, 18))))
    print(Solution().merge([Interval(1,4), Interval(5, 6), Interval(8, 10), Interval(15, 18)]))


# Just go through the intervals sorted by start coordinate and either combine the current interval
# with the previous one if they overlap, or add it to the output by itself if they don't.
#
# def merge(self, intervals):
#     out = []
#     for i in sorted(intervals, key=lambda i: i.start):
#         if out and i.start <= out[-1].end:
#             out[-1].end = max(out[-1].end, i.end)
#         else:
#             out += i,
#     return out

# Here is the fastest solution in leetcode.
# He use dict to save the status.And traverse sorted(dict.key()) array.
# When element is the start,then make in_segment = True.The group of data is saved until it hits end.
# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#
#         dict = {}
#         for interval in intervals:
#             if interval.start in dict:
#                 dict[interval.start][0] += 1
#             else:
#                 dict[interval.start] = [1, 0]
#
#             if interval.end in dict:
#                 dict[interval.end][1] += 1
#             else:
#                 dict[interval.end] = [0, 1]
#
#         keys = sorted(dict.keys())
#
#         print(keys)
#         result = []
#         count = 0
#         begin_idx = -1
#         in_segment = False
#         for point in keys:
#             count = count + dict[point][0] - dict[point][1]
#             if count > 0:
#                 if not in_segment:
#                     begin_idx = point
#                     in_segment = True
#             else:
#                 if not in_segment:
#                     begin_idx = point
#                 result.append([begin_idx, point])
#                 in_segment = False
#
#         return result

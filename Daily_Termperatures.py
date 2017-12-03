# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a list of daily temperatures, produce a list that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
# your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# Note: The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].

# Leetcode Weekly Contest 61.
# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 1628 ms
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        occurred_tems = {}
        for i in range(len(temperatures) - 1, -1, -1):
            interval = float('inf')
            for t in range(temperatures[i] + 1, 101):
                if t in occurred_tems:
                    interval = min(interval, occurred_tems[t] - i)
            occurred_tems[temperatures[i]] = i  # if occurred_tems has the same value, set the value is the nearest day.
            ans[i] = interval if interval != float('inf') else ans[i]
        return ans


if __name__ == '__main__':
    print(Solution().dailyTemperatures(
        [73, 74, 75, 71, 69, 72, 76, 73]
    ))

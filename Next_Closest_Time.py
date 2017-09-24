# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = time[:2] + time[3:]
        res = []

        def dfs(digits, path, res):
            if len(path) == 4:
                res.append(path)
                return
            for i in range(len(digits)):
                dfs(digits, path+digits[i], res)

        dfs(digits, '', res)
        closest_time = max(res)

        for r in res:
            if r[0] > '2' or r[:2] >= '24' or r[2] >= '6':
                continue
            if digits >= r:
                r = int(r) + 2400
            closest_time = min(str(closest_time), str(r))

        if int(closest_time) > int(2400):
            closest_time = str(int(closest_time) - 2400)
        return closest_time[:2] + ':' + closest_time[2:]

if __name__ == '__main__':
    print(Solution().nextClosestTime('19:34'))
    print(Solution().nextClosestTime('23:59'))
    print(Solution().nextClosestTime("13:55"))

# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 55 ms
# Your runtime beats 100.00 % of python submissions.



# Here solution is so cool!
# Just turn the clock forwards one minute at a time until a time with the original digits is reached.
from datetime import *
class Solution(object):
    def nextClosestTime(self, time):
        digits = set(time)
        while True:
            time = (datetime.strptime(time, '%H:%M') + timedelta(minutes=1)).strftime('%H:%M')
            if set(time) <= digits:  # if a is subset of b, then a < b is true.
                return time


# The idea is really simple.
# Generate all increments of the time given, and find the first time that has all the digits in the original time given.
def nextClosestTime(self, time):
    digits = [int(y) for x in time.split(':') for y in x]
    h, m = time.split(':')[0], time.split(':')[1]  # It would be better to use h, m = time.split(':')
    while True:
        h, m = (str(int(h)+1), '00') if int(m) == 59 else (h, str(int(m)+1))
        h = '00' if int(h) > 23 else h
        h = '0' + h if len(h) == 1 else h
        m = '0' + m if len(m) == 1 else m
        if all([int(x) in digits for x in h+m]):
            return h + ':' + m

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Implement a MyCalendar class to store your events.
# A new event can be added if adding the event will not cause a double booking.
# Your class will have the method, book(int start, int end).
# Formally, this represents a booking on the half open interval [start, end),
# the range of real numbers x such that start <= x < end.
# A double booking happens when two events have some non-empty intersection
# (ie., there is some time that is common to both events.)
# For each call to the method MyCalendar.book,
# return true if the event can be added to the calendar successfully without causing a double booking. Otherwise,
# return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
# Example 1:
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(15, 25); // returns false
# MyCalendar.book(20, 30); // returns true
# Explanation:
# The first event can be booked.  The second can't because time 15 is already booked by another event.
# The third event can be booked, as the first event takes every time less than 20, but not including 20.

# Leetcode Weekly Contest 59.
# 108 / 108 test cases passed.
# Status: Accepted
# Runtime: 1059 ms
class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in self.calendar:
            # Two Situations: 1. ( () ) not matter intersect or include. 2. () () not matter who is bigger.
            # If max(a.start, b.start) < min(a.end , b.end) that's mean they have intersection.
            if max(i[0], start) < min(i[1], end):
                # (start => i[1] or end <= i[0]) is not intersection.
                return False
        self.calendar += (start, end),
        return True

        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)

# Binary Search
# 108 / 108 test cases passed.
# Status: Accepted
# Runtime: 256 ms
import bisect
class MyCalendar(object):
    def __init__(self):
        self.calendar = []
        self._start_sorted = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.calendar:
            self.calendar += (start, end),
            self._start_sorted += start,
            return True
        floor_index = bisect.bisect_left(self._start_sorted, start)
        if floor_index and self.calendar[floor_index - 1][1] > start:
                return False

        ceiling_index = bisect.bisect_right(self._start_sorted, start)
        if self.calendar[ceiling_index - 1][0] == start and self.calendar[ceiling_index - 1][0] < end:
                return False
        elif ceiling_index != len(self.calendar) and self.calendar[ceiling_index][0] < end:
                return False

        self.calendar.insert(floor_index, (start, end))
        self._start_sorted.insert(floor_index, start)
        return True


if __name__ == '__main__':
    mycalendar = MyCalendar()
    print(mycalendar.book(47, 50))
    print(mycalendar.book(33, 41))
    print(mycalendar.book(39, 45))
    print(mycalendar.book(33, 42))
    print(mycalendar.book(25, 32))
    print(mycalendar.book(26, 35))
    print(mycalendar.book(19, 25))
    print(mycalendar.book(3, 8))
    print(mycalendar.book(8, 13))
    print(mycalendar.book(18, 27))

    # print(mycalendar.book(10, 20))
    # print(mycalendar.book(15, 25))
    # print(mycalendar.book(20, 30))

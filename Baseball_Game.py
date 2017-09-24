# -*- encoding:utf-8 -*-
# __author__=='Gan'


# 682. Baseball Game My SubmissionsBack to Contest
# User Accepted: 0
# User Tried: 0
# Total Accepted: 0
# Total Submissions: 0
# Difficulty: Easy
# You're now a baseball game point recorder.
#
# Given a list of strings, each string can be one of the 4 following types:
#
# Integer (one round's score): Directly represents the number of points you get in this round.
# "+" (one round's score):
#  Represents that the points you get in this round are the sum of the last two valid round's points.
# "D" (one round's score):
#  Represents that the points you get in this round are the doubled data of the last valid round's points.
# "C" (an operation,
#  which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
# Each round's operation is permanent and could have an impact on the round before and the round after.
# You need to return the sum of the points you could get in all the rounds.

# Example 2:
# Input: ["5","-2","4","C","D","9","+","+"]
# Output: 27
# Explanation:
# Round 1: You could get 5 points. The sum is: 5.
# Round 2: You could get -2 points. The sum is: 3.
# Round 3: You could get 4 points. The sum is: 7.
# Operation 1: The round 3's data is invalid. The sum is: 3.
# Round 4: You could get -4 points (the round 3's data has been removed). The sum is: -1.
# Round 5: You could get 9 points. The sum is: 8.
# Round 6: You could get -4 + 9 = 5 points. The sum is 13.
# Round 7: You could get 9 + 5 = 14 points. The sum is 27.


class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        if len(ops) < 1:
            return 0

        lo, hi = 0, len(ops)
        sum_ = 0
        while lo < hi:
            if ops[lo] == 'C':
                sum_ -= int(ops.pop(lo - 1))
                ops.pop(lo - 1)
                hi -= 2
                lo -= 1
                continue
            elif ops[lo] == 'D':
                ops[lo] = int(ops[lo - 1]) * 2
                sum_ += ops[lo]
                lo += 1
            elif ops[lo] == '+':
                ops[lo] = int(ops[lo - 1]) + int(ops[lo - 2])
                sum_ += ops[lo]
                lo += 1
            else:
                sum_ += int(ops[lo])
                lo += 1
        return sum_


#  Concise solution:
class Solution(object):
    def calPoints(self, ops):
        # Time: O(n)
        # Space: O(n)
        history = []
        for op in ops:
            if op == 'C':
                history.pop()
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == '+':
                history.append(history[-1] + history[-2])
            else:
                history.append(int(op))
        return sum(history)


if __name__ == '__main__':
   print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]))


# 38 / 38 test cases passed.
# Status: Accepted
# Runtime: 46 ms
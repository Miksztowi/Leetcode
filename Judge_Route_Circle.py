# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
# judge if this robot makes a circle, which means it moves back to the original place.
# The move sequence is represented by a string. And each move is represent by a character.
# The valid robot moves are R (Right), L (Left), U (Up) and D (down).
# The output should be true or false representing whether the robot makes a circle.
# Example 1:
# Input: "UD"
# Output: true
# Example 2:
# Input: "LL"
# Output: false


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 68.81 % of python submissions.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        str2move = {'U': 2, 'D': -2, 'L': 3, 'R': -3}
        return sum([str2move[move] for move in moves]) == 0


# 62 / 62 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# Your runtime beats 70.23 % of python submissions.
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')

if __name__ == '__main__':
    print(Solution().judgeCircle('LL'))
    print(Solution().judgeCircle('UD'))
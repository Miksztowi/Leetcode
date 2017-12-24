# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
# '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around:
# for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
# the wheels of the lock will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number
# of turns required to open the lock, or -1 if it is impossible.
# Example 1:
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# Example 2:
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation:
# We can turn the last wheel in reverse to move from "0000" -> "0009".
# Example 3:
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation:
# We can't reach the target without getting stuck.
# Example 4:
# Input: deadends = ["0000"], target = "8888"
# Output: -1
# Note:
# The length of deadends will be in the range [1, 500].
# target will not be in the list deadends.
# Every string in deadends and the string target will be a string of 4 digits from
# the 10,000 possibilities '0000' to '9999'.

# LeetCode Weekly Contest 64.
# 40 / 40 test cases passed.
# Status: Accepted
# Runtime: 1125 ms
# BFS,  Avoiding to handle the same node, we should use queue and visited list.
from collections import deque
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        marker, depth = 'x', 0
        q, visited, deadends = deque(['0000', marker]), set(), set(deadends)

        def generate(node):
            res = []
            for i, v in enumerate(node):
                num = int(v)
                res.append(node[:i] + str(9 if num == 0 else num - 1) + node[i + 1:])
                res.append(node[:i] + str(0 if num == 9 else num + 1) + node[i + 1:])
            return res

        while q:
            node = q.popleft()
            if node == target:
                return depth
            if node in deadends or node in visited:
                continue
            if node == marker and not q:
                return -1
            if node == marker:
                depth += 1
                q.append(marker)
            else:
                q.extend(generate(node))
                visited.add(node)
        return -1


if __name__ == '__main__':
    print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
    # print(Solution().openLock(["8888"], "0009"))
    # print(Solution().openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"))

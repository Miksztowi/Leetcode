# -*- encoding:utf-8 -*-
# __author__=='Gan'

# In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other
# rabbits have the same color as them. Those answers are placed in an array.
# Return the minimum number of rabbits that could be in the forest.
# Examples:
# Input: answers = [1, 1, 2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit than answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
# Input: answers = [10, 10, 10]
# Output: 11
# Input: answers = []
# Output: 0
# Note:
# answers will have length at most 1000.
# Each answers[i] will be an integer in the range [0, 999].


# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 52 ms
from collections import Counter
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        counter = Counter(answers)
        res = counter[0]
        for i in counter:
            if i:
                while counter[i] > 0:
                    res += i + 1
                    counter[i] -= i + 1
        return res


if __name__ == '__main__':
    print(Solution().numRabbits([1, 1, 2]))
    print(Solution().numRabbits([10, 10, 10]))
    print(Solution().numRabbits([0, 0, 1, 1, 1]))
    print(Solution().numRabbits([2, 1, 2, 2, 2, 2, 2, 2, 1, 1]))

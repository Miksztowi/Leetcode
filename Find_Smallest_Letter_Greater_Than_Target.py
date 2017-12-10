# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
# find the smallest element in the list that is larger than the given target.
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
# Examples:
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
# Note:
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.

# 165 / 165 test cases passed.
# Status: Accepted
# Runtime: 66 ms
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for l in letters:
            if l > target:
                return l

        return letters[0]


# 165 / 165 test cases passed.
# Status: Accepted
# Runtime: 52 ms
import bisect
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        pos = bisect.bisect_right(letters, target)
        return letters[0] if pos == len(letters) else letters[pos]


if __name__ == '__main__':
    print(Solution().nextGreatestLetter(
        ["c", "f", "j"], 'k'
    ))

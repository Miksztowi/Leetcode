# -*- encoding:utf-8 -*-
# __author__=='Gan'

# We are stacking blocks to form a pyramid. Each block has a color which is a one letter string, like `'Z'`.
# For every block of color `C` we place not in the bottom row,
# we are placing it on top of a left block of color `A` and right block of color `B`.
# We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
# We start with a bottom row of bottom, represented as a single string.
# We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.
# Return tr
#
#
#
# w a ue if we can build the pyramid all the way to the top, otherwise false.
# Example 1:
# Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
#     A
#    / \
#   D   E
#  / \ / \
# X   Y   Z
#
# This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
# Example 1:
# Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

from collections import defaultdict
from itertools import product


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        top = len(bottom)
        hash_map = defaultdict(set)
        for a in allowed:
            hash_map[a[:2]].add(a[2])
        next_bottoms = {bottom}

        cur_level = top
        while next_bottoms:
            temp = []
            cur_level -= 1
            if 1 == cur_level:
                return True
            for next_bottom in next_bottoms:
                i = ''
                for i in range(len(next_bottom) - 1):
                    if hash_map.get(next_bottom[i] + next_bottom[i + 1]):
                        i = i + hash_map.get(next_bottom[i] + next_bottom[i + 1])
                if len(i) >= cur_level:
                    temp += i,
            if not temp:
                return False
            print(temp)
            next_bottoms = temp



if __name__ == '__main__':
    print(Solution().pyramidTransition('XXYX', ["XXX", "XXY", "XYX", "XYY", "YXZ"]))
    print(Solution().pyramidTransition('', []))
    print(Solution().pyramidTransition('XYZ', ["XYD", "YZE", "DEA", "FFF"]))
    print(Solution().pyramidTransition("AABCCBABBB",
                                       ["AAA", "AAB", "BCD", "BCA", "BCB", "BAD", "BAB", "BAA", "CCD", "BDD", "CCA",
                                        "CAA", "CAD", "DAD", "DAA", "DAC", "DCD", "DCB", "DCA", "CDD", "ABA", "ABB",
                                        "BBC", "BBB", "BBA", "ADC", "CBB", "CBA", "CDB", "CDC", "DBC", "DBB"]))
    print(Solution().pyramidTransition("ABDBACAAAC",
                                       ["ACC", "AAC", "AAB", "BCB", "BAD", "CAC", "CCD", "CAA", "CCB", "DAD", "ACD",
                                        "DCB", "ABB", "BDA", "BDC", "BDB", "BBD", "BBC", "BBB", "ADB", "ADC", "DDC",
                                        "DDB", "CDD", "CBC", "CBA", "CBD", "CDC", "DBC"]))

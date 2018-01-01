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

# 32 / 32 test cases passed.
# Status: Accepted
# Runtime: 408 ms
# We model the states that blocks could be in. We can do this using binary: a number like 0b0001011 would correspond to
# the state of the block being either 'A', 'B' or 'D'.
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        T = [[0] * 7 for _ in range(7)]
        for tripe in allowed:
            a, b, c = map(ord, tripe)
            T[a - ord('A')][b - ord('A')] |= 1 << (c - ord('A'))

        state = [1 << (ord(x) - ord('A')) for x in bottom]

        for loops in bottom[:-1]:
            for i in range(len(state) - 1):
                k = 0
                for b1 in range(7):
                    if (state[i] >> b1) & 1:
                        for b2 in range(7):
                            if (state[i + 1] >> b2) & 1:
                                k |= T[b1][b2]
                state[i] = k
            state.pop()
        return bool(state[0])




if __name__ == '__main__':
    # print(Solution().pyramidTransition('XXYX', ["XXX", "XXY", "XYX", "XYY", "YXZ"]))
    # print(Solution().pyramidTransition('', []))
    # print(Solution().pyramidTransition('XYZ', ["XYD", "YZE", "DEA", "FFF"]))
    print(Solution().pyramidTransition("AABCCBABBB",
                                       ["AAA", "AAB", "BCD", "BCA", "BCB", "BAD", "BAB", "BAA", "CCD", "BDD", "CCA",
                                        "CAA", "CAD", "DAD", "DAA", "DAC", "DCD", "DCB", "DCA", "CDD", "ABA", "ABB",
                                        "BBC", "BBB", "BBA", "ADC", "CBB", "CBA", "CDB", "CDC", "DBC", "DBB"]))
    print(Solution().pyramidTransition("ABDBACAAAC",
                                       ["ACC", "AAC", "AAB", "BCB", "BAD", "CAC", "CCD", "CAA", "CCB", "DAD", "ACD",
                                        "DCB", "ABB", "BDA", "BDC", "BDB", "BBD", "BBC", "BBB", "ADB", "ADC", "DDC",
                                        "DDB", "CDD", "CBC", "CBA", "CBD", "CDC", "DBC"]))

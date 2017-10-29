# -*- encoding:utf-8 -*-
# __author__=='Gan'

# LeetCode Weekly Contest 56.
# We have two special characters. The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
# Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
# The given string will always end with a zero.
# Example 1:
# Input:
# bits = [1, 0, 0]
# Output: True
# Explanation:
# The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
# Example 2:
# Input:
# bits = [1, 1, 1, 0]
# Output: False
# Explanation:
# The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

# Iterating the bits, if two-bit lo += 2, else if one-bit lo +=1.
# Break loop when lo > hi - 1, and return True if lo == hi - 1.
# 93 / 93 test cases passed.
# Status: Accepted
# Runtime: 36 ms
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits or bits[-1] != 0:
            return False

        lo, hi = 0, len(bits)

        if hi == 1:
            return True

        while lo < hi - 1:
            if bits[lo] == 1:
                lo += 1
            lo += 1

        return lo == hi - 1

# Single Regular Expression.
# 93 / 93 test cases passed.
# Status: Accepted
# Runtime: 39 ms
import re
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        return True if re.match(r'^(10|11|0)*0$', ''.join([str(x) for x in bits])) else False


if __name__ == '__main__':
    print(Solution().isOneBitCharacter([0]))
    print(Solution().isOneBitCharacter([1, 0, 0]))
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
# "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        flips = [0]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                flips.append(i)
        flips.append(len(s))
        chunks = [(a-b) for a, b in zip(flips[1:], flips)]
        print(chunks)
        return sum(min(a, b) for a, b in zip(chunks, chunks[1:]))


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(s, s[1:]))


if __name__ == '__main__':
    print(Solution().countBinarySubstrings('00110011'))
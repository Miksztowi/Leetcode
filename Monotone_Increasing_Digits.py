# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-negative integer N, find the largest number that is less than or equal
# to N with monotone increasing digits.
# (Recall that an integer has monotone increasing digits if and only if each pair
# of adjacent digits x and y satisfy x <= y.)
# Example 1:
# Input: N = 10
# Output: 9
# Example 2:
# Input: N = 1234
# Output: 1234
# Example 3:
# Input: N = 332
# Output: 299
# Note: N is an integer in the range [0, 10^9].

# Leetcode Weekly Contest 61.
# 302 / 302 test cases passed.
# Status: Accepted
# Runtime: 42 ms
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = [int(x) for x in str(N)[::-1]]
        inver_idx = -1
        for i in range(1, len(digits)):
            if digits[i - 1] < digits[i] or (inver_idx != -1 and digits[inver_idx] == digits[i]):
                inver_idx = i

        if inver_idx == -1:
            return N

        for i in range(inver_idx):
            digits[i] = 9
        digits[inver_idx] -= 1
        return int(''.join([str(x) for x in digits[::-1]]))


if __name__ == '__main__':
    # print(Solution().monotoneIncreasingDigits(
    #     1234
    # ))
    # print(Solution().monotoneIncreasingDigits(332))
    # print(Solution().monotoneIncreasingDigits(500))
    print(Solution().monotoneIncreasingDigits(668841))

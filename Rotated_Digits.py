# -*- encoding:utf-8 -*-
# __author__=='Gan'

# X is a good number if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from X. A number is valid if each digit remains a digit after rotation. 0, 1,
# and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other,
# and the rest of the numbers do not rotate to any other number.
# Now given a positive number N, how many numbers X from 1 to N are good?
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# Note:
# N  will be in range [1, 10000].

# Leetcode Contest 73.
# 50 / 50 test cases passed.
# Status: Accepted
# Runtime: 176 ms
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        changed = False
        change_nums = ['2', '5', '6', '9']
        unchange_nums = ['1', '0', '8']
        for i in range(N + 1):
            for s in str(i):
                if s not in (change_nums + unchange_nums):
                    changed = False
                    break
                if s in change_nums:
                    changed = True
            cnt += 1 if changed else 0
            changed = False
        return cnt


if __name__ == '__main__':
    print(Solution().rotatedDigits(10))
    print(Solution().rotatedDigits(857))
    

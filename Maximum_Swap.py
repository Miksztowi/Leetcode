# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.
#
# Example 1:
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# Example 2:
# Input: 9973
# Output: 9973
# Explanation: No swap.
# Note:
# The given number is in the range [0, 10**8]


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        dummy = list(str(num))
        digit_dict = {int(x): i for i, x in enumerate(dummy)}
        print(digit_dict)
        for i, x in enumerate(dummy):
            for j in range(9, int(x), -1): # use this iter, will filter the digit what all > x.
                if digit_dict.get(j, 0) > i:
                    dummy[digit_dict[j]], dummy[i] = dummy[i], dummy[digit_dict[j]]
                    return ''.join(dummy)
        return num
# 111 / 111 test cases passed.
# Status: Accepted
# Runtime: 45 ms


# Here is the fast solution in Leetcode.
# class Solution(object):
#     def maximumSwap(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#         numLst = list(str(num))
#         minIdx = -1
#         mxItemIdx = 0
#         for i in range(1, len(numLst)):
#             if numLst[i] > numLst[i - 1] and minIdx == -1:
#                 minIdx = i - 1
#                 mxItemIdx = i
#             elif numLst[i] >= numLst[mxItemIdx]:
#                 mxItemIdx = i
#
#         if minIdx != -1:
#             for i in range(minIdx + 1):
#                 if numLst[i] < numLst[mxItemIdx]:
#                     tmp = numLst[i]
#                     numLst[i] = numLst[mxItemIdx]
#                     numLst[mxItemIdx] = tmp
#                     return int(''.join(numLst))
#
#         return num
if __name__ == '__main__':
    print(Solution().maximumSwap(7236))



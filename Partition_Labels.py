# -*- encoding:utf-8 -*-
# __author__=='Gan'

# A string S of lowercase letters is given.
# We want to partition this string into as many parts as possible so that each letter appears in at most one part,
# and return a list of integers representing the size of these parts.
# Example 1:
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.


# 116 / 116 test cases passed.
# Status: Accepted
# Runtime: 93 ms
# Leetcode Weekly Contest 67.
# for-else statement make concise.
from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        letters_counter = Counter(S)
        partitions = []
        tmp_s = ''
        tmp_l = set()
        for i in range(len(S)):
            tmp_s = tmp_s + S[i]
            letters_counter[S[i]] -= 1
            if S[i] not in tmp_l:
                tmp_l.add(S[i])
            for e in tmp_l:
                if letters_counter[e] != 0:
                    break
            else:
                partitions.append(len(tmp_s))
                tmp_s = ''
                tmp_l = set()
        return partitions



if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
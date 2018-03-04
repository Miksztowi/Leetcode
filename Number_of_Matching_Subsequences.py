# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# Note:
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].

# LeetCode Weekly Contest 74.
# 49 / 49 test cases passed.
# Status: Accepted
# Runtime: 940 ms
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def is_match(word, w_i, d_i):
            if w_i == len(word):
                return True
            l = idxs_dict.get(word[w_i], [])
            if len(l) == 0 or d_i > l[-1]:
                return False
            # To speed up the processing, we should use binary search in the index dictionary.
            i = l[bisect_left(l, d_i)]
            return is_match(word, w_i + 1, i + 1)

        idxs_dict = defaultdict(list)

        for i in range(len(S)):
            idxs_dict[S[i]].append(i)
        return sum(is_match(word, 0, 0) for word in words)


if __name__ == '__main__':
    print(Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))

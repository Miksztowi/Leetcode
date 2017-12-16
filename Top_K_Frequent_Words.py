# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency,
# then the word with the lower alphabetical order comes first.
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.


# 110 / 110 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 86.51 % of python submissions.
import heapq
import collections


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_fre = collections.defaultdict(int)
        for word in words:
            words_fre[word] += 1

        heap = []
        for word in words_fre:
            heapq.heappush(heap, (-words_fre[word], word))

        return [x[1] for x in sorted(heap, key=lambda x: (x[0], x[1]))[:k]]


if __name__ == '__main__':
    print(Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
    print(Solution().topKFrequent(["a", "aa", "aaa"], 2))

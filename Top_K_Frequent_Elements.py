# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-empty array of integers, return the k most frequent elements.
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


# 20 / 20 test cases passed.
# Status: Accepted
# Runtime: 65 ms
# Your runtime beats 56.14 % of python submissions.
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        ans = sorted(count, key=lambda x: count[x], reverse=True)
        return ans[:k]


# 20 / 20 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 90.07 % of python submissions.
import collections
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = collections.defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        heap = []
        for freq in freq_map:
            if len(heap) < k:
                heapq.heappush(heap, (freq_map[freq], freq))
            elif freq_map[freq] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq_map[freq], freq))
        return [heapq.heappop(heap)[1] for x in range(k)]


if __name__ == '__main__':
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

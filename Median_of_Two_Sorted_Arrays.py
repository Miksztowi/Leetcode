# -*- encoding:utf-8 -*-
# __author__=='Gan'

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        index_a, index_b = 0, 0
        merged_list, index_m = [], 0
        total_length = len(nums1) + len(nums2)

        while index_a < len(nums1) and index_b < len(nums2):
            if nums1[index_a] < nums2[index_b]:
                merged_list.append(nums1[index_a])
                index_a += 1
            else:
                merged_list.append(nums2[index_b])
                index_b += 1
        if index_a < len(nums1):
            merged_list += nums1[index_a:]
        if index_b < len(nums2):
            merged_list += nums2[index_b:]

        median_index = (total_length - 1) // 2
        if total_length % 2 and total_length > 1:
            median = merged_list[median_index]
        elif total_length == 1 :
            median = merged_list[0]
        else:
            median = (merged_list[median_index] + merged_list[median_index + 1]) / 2
        return median


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3], [2,5]))
    print(Solution().findMedianSortedArrays([], [2,3]))

# 2080 / 2080 test cases passed.
# Status: Accepted
# Runtime: 252 ms
# Accepted Solutions Runtime Distribution
#
# Sorry. We do not have enough accepted submissions to show runtime distribution chart.
# Invite friends to challenge Median of Two Sorted Arrays !
# hmmmm, it's my first time to see this!!!!!
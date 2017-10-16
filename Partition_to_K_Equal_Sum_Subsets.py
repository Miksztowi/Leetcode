# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of integers nums and a positive integer k,
# find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums or len(nums) < k:
            return False
        if k == 1:
            return True

        def is_k_partition_possible_rec(nums, subset_sum, taken,
                                        subset, k, n, cur_index, limit_index):
            if subset_sum[cur_index] == subset:
                if cur_index == k - 2:  # cur_index + 1 == k - 1:
                    return True
                return is_k_partition_possible_rec(nums, subset_sum, taken, subset, k, n, cur_index+1, n-1)

            for i in range(limit_index, -1, -1):
                if taken[i]:
                    continue
                tmp = subset_sum[cur_index] + nums[i]

                if tmp <= subset:
                    subset_sum[cur_index] += nums[i]
                    taken[i] = True
                    next_ = is_k_partition_possible_rec(nums, subset_sum, taken, subset, k, n, cur_index, i-1)

                    taken[i] = False
                    subset_sum[cur_index] -= nums[i]

                    if next_:
                        return True
            return False

        subset = sum(nums) // k

        if subset != sum(nums) / k:
            return False

        taken = [False] * len(nums)
        subset_sum = [0] * k
        subset_sum[0] = nums[len(nums) - 1]
        taken[len(nums) - 1] = True

        return is_k_partition_possible_rec(nums, subset_sum, taken, subset, k, len(nums), 0, len(nums) - 1)


if __name__ == '__main__':
    print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
    print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3))


# 141 / 141 test cases passed.
# Status: Accepted
# Runtime: 149 ms
# http://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/

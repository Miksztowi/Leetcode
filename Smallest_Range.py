# -*- encoding:utf-8 -*-
# __author__=='Gan'


# You have k lists of sorted integers in ascending order.
# Find the smallest range that includes at least one number from each of the k lists.
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
# Example 1:
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Note:
# The given list may contain duplicates, so ascending order means >= here.
# 1 <= k <= 3500
# -105 <= value of elements <= 105.
# For Java users, please note that the input type has been changed to List<List<Integer>>.
# And after you reset the code template, you'll see this point.



# 86 / 86 test cases passed.
# Status: Accepted
# Runtime: 226 ms
# Your runtime beats 87.70 % of python submissions.
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        all_hash_nums = []
        items_count = {i: 0 for i in range(len(nums))}
        J = I = i = 0
        missing = len(nums)
        for k, item in enumerate(nums):  # if use i replace k, here cause i was changed.
            for num in item:
                all_hash_nums += (num, k),
        all_hash_nums.sort(key=lambda x: x[0])

        for j, v in enumerate(all_hash_nums):
            if items_count[v[1]] == 0:  # Only first time will make missing subtract 1.
                missing -= 1
            items_count[v[1]] += 1
            if not missing:
                while i < j and items_count[all_hash_nums[i][1]] > 1:
                    items_count[all_hash_nums[i][1]] -= 1
                    i += 1
                if not J or all_hash_nums[J][0] - all_hash_nums[I][0] > all_hash_nums[j][0] - all_hash_nums[i][0]:
                    J = j
                    I = i
        return [all_hash_nums[I][0], all_hash_nums[J][0]]


if __name__ == '__main__':
    print(Solution().smallestRange(
        [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    ))

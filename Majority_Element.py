# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
class Solution(object):
    # Time complexity: O(n)
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            return nums[-1]
        count_dict = {}
        for num in nums:
            if count_dict.get(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] > len(nums) // 2:
                return num


# Because the problem describes that the majority element always exist in the array.
# So the index of middle is the answer.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


def majorityElement5(nums):
    bit = [0] * 32
    for num in nums:
        for j in range(32):
            bit[j] += num >> j & 1
    print(bit)
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums) // 2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1 << 31) - res)
            else:
                res |= 1 << i
    return res


if __name__ == '__main__':
    print(majorityElement5([1,2,2,3,3,3]))
    # print(Solution().majorityElement([1, 2, 2, 2, 3]))
    # print(Solution().majorityElement([1]))
    # print(Solution().majorityElement([1, 2, 2]))
    # print(Solution().majorityElement([1, 2]))


# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 76.34 % of python submissions.


# Bit manipulation
def majorityElement5(self, nums):
    bit = [0] * 32
    for num in nums:
        for j in range(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums) // 2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1 << 31) - res)
            else:
                res |= 1 << i
    return res


# Divide and Conquer
def majorityElement6(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = self.majorityElement(nums[:len(nums) // 2])
    b = self.majorityElement(nums[len(nums) // 2:])
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums) // 2]


# the idea here is if a pair of elements from the
# list is not the same, then delete both, the last
# remaining element is the majority number
def majorityElement(self, nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:
            count += 1
        elif count == 0:
            cand, count = num, 1
        else:
            count -= 1
    return cand

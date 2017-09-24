# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

# If 0 in nums, the solution failed.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest_product = max(nums)
        cur_product = nums[0]
        negative_product = 1
        for i in range(1, len(nums)):
            if cur_product * nums[i] <= cur_product:
                if negative_product == 1:
                    negative_product = cur_product * nums[i]
                    cur_product = 1
                else:
                    cur_product = negative_product * cur_product * nums[i]
                    negative_product = 1
            else:
                cur_product *= nums[i]

            if cur_product > largest_product:
                largest_product = cur_product

        return largest_product


# Use swap(max_, min_) to handle negative
# Use max() and min() to handle 0.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_, min_ = nums[0], nums[0]
        largest_product = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_, min_ = min_, max_

            max_ = max(num, max_ * num)
            min_ = min(num, min_ * num)

            largest_product = max(max_, largest_product)

        return largest_product


if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([0, 2]))
    print(Solution().maxProduct([-1, 0, -2]))


# Concise solution.
def maxProduct(nums):
    maximum = big = small = nums[0]
    for n in nums[1:]:
        big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        # Just like a, b = b, a
        maximum = max(maximum, big)
    return maximum


# But!!!!! This solution will get mistake.
def maxProduct(self, nums):
    maximum = big = small = nums[0]
    for n in nums[1:]:
        big = max(n, n * big, n * small)
        small = min(n, n * big, n * small)
        # Due to big has been updated, so small will get wrong result.
        # In [257]: dis.dis('a=1; a, b = 0, a')
        # 1           0 LOAD_CONST               0 (1)
        #             3 STORE_NAME               0 (a)
        #             6 LOAD_CONST               1 (0)
        #             9 LOAD_NAME                0 (a)
        #            12 ROT_TWO
        #            13 STORE_NAME               0 (a)
        #            16 STORE_NAME               1 (b)
        #            19 LOAD_CONST               2 (None)
        #            22 RETURN_VALUE
        maximum = max(maximum, big)
    return maximum


# Notice
a = [1]
b = a
b += [1]  # Then a = [1,1]
b = b + [1]  # Then a = [1]


class Solution2:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        global_max, local_max, local_min = float("-inf"), 1, 1
        for x in A:
            local_max = max(1, local_max)  # To handle the zero.
            if x > 0:
                local_max, local_min = local_max * x, local_min * x
            else:
                local_max, local_min = local_min * x, local_max * x
            global_max = max(global_max, local_max)
        return global_max

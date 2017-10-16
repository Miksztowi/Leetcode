# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
# find the duplicate one.
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 53 / 53 test cases passed.
# Status: Accepted
# Runtime: 72 ms
# Your runtime beats 17.27 % of python submissions.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo + 1 < hi:
            count = 0
            mid = (lo + hi) // 2
            for num in nums:
                if mid < num <= hi:
                    count += 1
            if count > hi - mid:
                lo = mid
            else:
                hi = mid
        return hi

# 53 / 53 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 72.54 % of python submissions.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Ideal from: http://keithschwarz.com/interesting/code/?dir=find-duplicate
        # We have to see the input array from a whole different angel.
        # This array in fact is a map(or route function) for a route, which is
        #   x_0 = 0             => Step 0: start from the position x_0
        #   f(1) => nums[x_0] = x_1     => Step 1: from x_0 go to x_1
        #   f(2) => nums[x_1] = x_2     => Step 2: from x_1 go to x_2
        #   ... ...
        #   f(i) => nums[x_i] = x_{i+1} => Step i: from x_i go to x_{i+1}.
        # If there was infinite nums, the route would go along forever without any position revisited.
        # If the nums was finite with no repeated position, the route would be a perfect circle loop.
        # If the nums was finite with repeated position, the route would be rho-shaped.
        # The key point is to find the start of the rho-shaped circle, x_c.
        # x_c is the dulpicated number.

        # To find x_c, we have to borrow Floyd 's "tortoise and hare" algorithm to find the x_l,
        # where f(stepsToL) = x_l == x_2l = f(doubleStepsToL) and
        # stepsToL is the smallest multiple of the length of the rho-shaped circle(rhoLen) larger than stepsToC.
        hare, tortoise = nums[nums[0]], nums[0]
        while hare != tortoise:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]

        hare = 0

        # After finding stepL, now we are able to find x_c.
        # Consider stepsToL is the smallest multiple of rhoLen larger than stepsToC.
        # Hence f(stepsToL) ends at f(stepC) plus (rhoLen - stepsToC) steps forward.
        # So we know we will reach f(stepsToC) again after stepC steps forward starting from f(stepsToL),
        # which is to find f(stepsToC) = f(stepsToL + stepsToC).
        while hare != tortoise:
            hare = nums[hare]
            tortoise = nums[tortoise]

        return tortoise


if __name__ == '__main__':
    print(Solution().findDuplicate([1,2,1,3,4]))

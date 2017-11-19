# -*- encoding:utf-8 -*-
# __author__=='Gan'
#
# A self-dividing number is a number that is divisible by every digit it contains.
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# Also, a self-dividing number is not allowed to contain the digit zero.
# Given a lower and upper number bound, output a list of every possible self dividing number,
# including the bounds if possible.
# Example 1:
# Input:
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

# Leetcode Weekly Contest 59.
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        def divide(divide_num, base=0):
            if base == len(str(divide_num)):
                return True
            if divide_num < 10 and divide_num != 0:
                return True
            num = int(str(divide_num)[base])
            if not num or divide_num % num:
                return False
            return divide(divide_num, base + 1)

        ans = filter(divide, range(left, right + 1))
        return list(ans)


# Elegant Solution
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        is_self_dividing = lambda num: '0' not in str(num) and all([num % int(i) == 0 for i in str(num)])
        return list(filter(is_self_dividing, range(left, right + 1)))


if __name__ == '__main__':
    print(Solution().selfDividingNumbers(1, 22))
    print(Solution().selfDividingNumbers(0, 0))

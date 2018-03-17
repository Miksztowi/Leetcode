# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# For example:
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

from functools import reduce


class Solution(object):
    def add_digits(self, num):
        """
        :type num: int
        :rtype: int
        """

        def rec_add(num):
            str_num = str(num)
            res = reduce(lambda a, b: int(a) + int(b), str_num)
            if int(res) > 9:
                return rec_add(res)
            return res

        return int(rec_add(num))


if __name__ == '__main__':
    assert Solution().add_digits(10) == 1
    assert Solution().add_digits(38) == 2
    assert Solution().add_digits(9) == 9
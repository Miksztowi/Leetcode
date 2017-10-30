# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an array of characters, compress it in-place.
#
# The length after compression must always be smaller than or equal to the original array.
#
# Every element of the array should be a character (not int) of length 1.
#
# After you are done modifying the input array in-place, return the new length of the array.
#
# Example 1:
# Input:
# ["a","a","b","b","c","c","c"]
#
# Output:
# Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
#
# Explanation:
# "aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
# Example 2:
# Input:
# ["a"]
#
# Output:
# Return 1, and the first 1 characters of the input array should be: ["a"]
#
# Explanation:
# Nothing is replaced.
# Example 3:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
#
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
#
# Explanation:
# Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
# Notice each digit has it's own entry in the array.


# Regular Expression.
# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 116 ms
import re
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        dummy_string = ''.join(chars)
        re_c = re.compile(r'(?<=(.))(\1+)')

        chars[:] = re_c.sub(lambda m: str(1 + len(m.group())), dummy_string)

        return len(chars)


# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 79 ms
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0

        lo, hi = 0, len(chars)
        same_element_length = 0

        while lo < hi:
            if lo + same_element_length < hi and chars[lo] == chars[lo + same_element_length]:
                same_element_length += 1
            else:
                if same_element_length > 1:
                    dummy_list = []
                    length = same_element_length
                    while same_element_length:
                        dummy_list.insert(0, str(same_element_length % 10))
                        same_element_length //= 10
                    chars[lo: lo + length] = [str(chars[lo])] + dummy_list
                    lo += len(dummy_list)
                    hi -= length - len(dummy_list) - 1
                lo += 1
                same_element_length = 0
        return len(chars)


# Functional Solution.
# 70 / 70 test cases passed.
# Status: Accepted
# Runtime: 99 ms
class Solution(object):
    def compress(self, chars):
        """
        :param chars:
        :return:
        """
        if not chars:
            return 0

        flips = [(chars[0], 0)] + [(chars[i], i) for i in range(1, len(chars)) if chars[i] != chars[i - 1]]\
                + [(None, len(chars))]
        chunks = [(b[0],a[1]-b[1]) for a, b in zip(flips[1:], flips)]
        from functools import reduce
        compressed = reduce(lambda x, y: x + [y[0]] + (list(str(y[1])) if (y[1] > 1) else []), chunks, [])
        chars[:len(compressed)] = compressed

        return len(compressed)


if __name__ == '__main__':
    print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
    print(Solution().compress(["a","a","a","b","b","a","a", "a"]))


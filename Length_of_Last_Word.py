# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip() # Use str.strip() to hanlde whitespace on the ends of the string.
        last_length, dummy = 0, list(s)
        for i in dummy[::-1]:
            if i != ' ':
                last_length += 1
            else:
                break
        return last_length


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))
    print(Solution().lengthOfLastWord("Ha"))
    print(Solution().lengthOfLastWord("a    "))
    print(Solution().lengthOfLastWord(" "))


# 59 / 59 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 58.54 % of python submissions.
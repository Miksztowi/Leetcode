# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parentheses_dict = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        for parenthese in s:
            if parentheses_dict.get(parenthese):
                stack.append(parenthese)
            elif len(stack) == 0 or parentheses_dict[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("([)]"))


# 73 / 73 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 60.87 % of python submissions.


# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 199 ms
# Your runtime beats 8.69 % of python submissions.
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ''
        temp = ''
        for i in s:
            if i != ' ':
                temp = i + temp
            else:
                ans += temp + ' '
                temp = ''
        return ans + temp


# 30 / 30 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 80.51 % of python submissions.
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(x[::-1] for x in s.split())


if __name__ == '__main__':
    print(Solution().reverseWords(
        "Let's take LeetCode contest"
    ))
    print(Solution().reverseWords(
        ""
    ))

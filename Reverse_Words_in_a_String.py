# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# Update (2015-02-12):
# For C programmers: Try to solve it in-place in O(1) space.


# 22 / 22 test cases passed.
# Status: Accepted
# Runtime: 35 ms
# Your runtime beats 46.36 % of python submissions.
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


# timeit.timeit('str_="The sky is bule,";" ".join(str_.split()[::-1])', number=10000000)
# Out[152]: 8.478504972998053
# timeit.timeit('str_="The sky is bule,";" ".join(reversed(str_.split())', number=10000000)
# Out[151]: 10.346161851994111

if __name__ == '__main__':
    print(Solution().reverseWords('the sky is blue'))
    print(Solution().reverseWords(''))

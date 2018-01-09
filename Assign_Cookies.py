# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie. Each child i has a greed factor gi,
# which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj.
# If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
# Example 1:
# Input: [1,2,3], [1,1]
# Output: 1
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
# Input: [1,2], [1,2,3]
# Output: 2
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.


# 21 / 21 test cases passed.
# Status: Accepted
# Runtime: 92 ms
# Your runtime beats 34.21 % of python submissions.
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        number = cookie = factor = 0
        s.sort()
        g.sort()
        while cookie < len(s) and factor < len(g):
            if s[cookie] >= g[factor]:
                number += 1
                cookie += 1
                factor += 1
            else:
                cookie += 1
        return number


if __name__ == '__main__':
    print(Solution().findContentChildren([1, 2, 3], [1, 1]))
    print(Solution().findContentChildren([1, 2, 3], [1, 2]))
    print(Solution().findContentChildren([], []))

# -*- encoding:utf-8 -*-
# __author__=='Gan'
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# I thought that following solutions.
# 1. Like Fibonacci Sequence, the n=1 has one case, and n=2 is changed on the basis of 1.etc....
# But it is too complex to distinguish the case.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []

        def generate(l, r, p, res= []):  # res is a tricks, but i don't support this operation.
            # if res is none:
            #    res = []  I think this is a better and safer operation. But it will take more time.
            if l: generate(l-1, r, p + '(')
            if l < r: generate(l, r-1, p + ')')
            if not r: res.append(p)
            return res
        return generate(n, n, '')



if __name__ == '__main__':
    print(Solution().generateParenthesis(3))


# 8 / 8 test cases passed.
# Status: Accepted
# Runtime: 46 ms
# Your runtime beats 56.01 % of python submissions.


# Here are some solutions from Leetcode. Cool but difficult to understand.
# Improved version of this.
# Parameter open tells the number of "already opened" parentheses,
# and I continue the recursion as long as
# I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).
def generateParenthesis(self, n, open=0):
    if n > 0 <= open:
        return ['(' + p for p in self.generateParenthesis(n-1, open+1)] + \
               [')' + p for p in self.generateParenthesis(n, open-1)]
    return [')' * open] * (not n)


# Improved version of this. Parameter open tells the number of "already opened" parentheses,
# and I continue the recursion as long as
# I still have to open parentheses (n > 0) and I haven't made a mistake yet (open >= 0).
def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:  # Here is a tricks. Don't like other Program language.
                                    # In python,it means left >= 0 and left <= right
            if not right:
                yield p
            for q in generate(p + '(', left-1, right): yield q
            for q in generate(p + ')', left, right-1): yield q

    return list(generate('', n, n))
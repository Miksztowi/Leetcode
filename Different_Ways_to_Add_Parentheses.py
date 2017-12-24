# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a string of numbers and operators, return all possible results from computing all the different possible ways
# to group numbers and operators. The valid operators are +, - and *.
# Example 1
# Input: "2-1-1".
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
# Example 2
# Input: "2*3-4*5"
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 49 ms
# Your runtime beats 43.80 % of python submissions.
# Divide-and-Conquer.
# Both res1 and res2 can product many situations, so it must preserve all of them.
# Otherwise it only get the last anwser.
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '-*+':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                [res.append(self.helper(int(r1), int(r2), input[i])) for r1 in res1 for r2 in res2]
                # Both res1 and res2 can product many situations, so it must preserve all of them.
                # Otherwise it only get the last anwser.
        return res

    def helper(self, j, k, op):
        if op == '*':
            return j * k
        elif op == '+':
            return j + k
        elif op == '-':
            return j - k


if __name__ == '__main__':
    print(Solution().diffWaysToCompute('2*3-4*5'))
    print(Solution().diffWaysToCompute('2*3'))

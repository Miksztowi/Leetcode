# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        digits_map = {
            '1': ['~'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            '0': ['~'],
        }
        res_list = ['']
        for digit in digits:
            res_list = [i + x for x in digits_map[digit] for i in res_list]
        # return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
        # If initial is present, it is placed before the items
        # of the sequence in the calculation, and serves as a default when the
        # sequence is empty.
        # In[181]: reduce(lambda x, y: x + y, [1, ], 1)
        # Out[181]: 2
        return res_list


if __name__ == '__main__':
    print(Solution().letterCombinations('23'))


# 25 / 25 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 15.18 % of python submissions.

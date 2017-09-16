# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += [(i, c), (c, j), (i//3, j//3, c)]
                    # if group is not unique, it means that sudoku is not valid.
                    # And  (i, c) (c, j ) are used to distinguish ('3', 3) and (3, '3').
        return len(seen) == len(set(seen))


if __name__ == '__main__':
    print(Solution().isValidSudoku(
        [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]))


# 501 / 501 test cases passed.
# Status: Accepted
# Runtime: 62 ms
# Your runtime beats 90.40 % of python submissions.



###### Here are some other solutions.
     # Use collections.Counter() is so cool.
# Idea
# Just go through all you see (like "7 in row 3") and check for duplicates.
# Solution 1
#
# Using Counter. One logical line, seven physical lines.
#
# def isValidSudoku(self, board):
#     return 1 == max(collections.Counter(
#         x
#         for i, row in enumerate(board)
#         for j, c in enumerate(row)
#         if c != '.'
#         for x in ((c, i), (j, c), (i/3, j/3, c))
#     ).values() + [1])
# The + [1] is only for the empty board, where max would get an empty list and complain. It's not necessary to get it accepted here, as the empty board isn't among the test cases, but it's good to have.
#
# Solution 2
#
# Using len(set).
#
# def isValidSudoku(self, board):
#     seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
#                 for i, row in enumerate(board)
#                 for j, c in enumerate(row)
#                 if c != '.'), [])
#     return len(seen) == len(set(seen))
# Solution 3
#
# Using any.
#
# def isValidSudoku(self, board):
#     seen = set()
#     return not any(x in seen or seen.add(x)
#                    for i, row in enumerate(board)
#                    for j, c in enumerate(row)
#                    if c != '.'
#                    for x in ((c, i), (j, c), (i/3, j/3, c)))
# Solution 4
#
# Iterating a different way.
#
# def isValidSudoku(self, board):
#     seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
#                 for i in range(9) for j in range(9)
#                 for c in [board[i][j]] if c != '.'), [])
#     return len(seen) == len(set(seen))
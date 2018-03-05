# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# For example,
# Given board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

# Your runtime beats 95.68 % of python3 submissions.
# 87 / 87 test cases passed.
# Status: Accepted
# Runtime: 256 ms
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(word, b_i, b_j):
            if len(word) == 0:
                return True
            if not (0 <= b_i < m and 0 <= b_j < n and board[b_i][b_j] == word[0]):
                return False
            tmp = board[b_i][b_j]
            board[b_i][b_j] = '#'
            res = dfs(word[1:], b_i, b_j + 1) or dfs(word[1:], b_i, b_j - 1) or dfs(word[1:], b_i + 1, b_j) or dfs(
                word[1:], b_i - 1, b_j)
            board[b_i][b_j] = tmp
            return res

        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if dfs(word, i, j):
                    return True
        return False


if __name__ == '__main__':
    print(Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCCED"))
    print(Solution().exist([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCCC"))

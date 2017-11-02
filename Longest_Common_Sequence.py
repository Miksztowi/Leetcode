# -*- encoding:utf-8 -*-
# __author__=='Gan'

# LCS
# 这题是算法课的实践题目， 所以打印方式与Leetcode有所不同。
import time

# Solution: Matrix
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length_A = len(A) + 1
        length_B = len(B) + 1

        start = time.time()
        DP = [[0 for _ in range(length_B)] for _ in range(length_A)]
        mark = [[False for _ in range(length_B)] for _ in range(length_A)]

        for i in range(1, length_A):
            for j in range(1, length_B):
                if A[i - 1] == B[j - 1]:
                    DP[i][j] = DP[i - 1][j - 1] + 1
                    mark[i][j] = '↖'
                elif DP[i - 1][j] >= DP[i][j - 1]:
                    DP[i][j] = DP[i - 1][j]
                    mark[i][j] = '↑'
                else:
                    DP[i][j] = DP[i][j - 1]
                    mark[i][j] = '←'

        def printf(memo):
            for i in range(1, len(memo)):
                print(['{:^4}'.format(memo[i][j]) for j in range(1, len(memo[i]))])

        def find_sequence(mark, i, j):
            if i == 0 or j == 0:
                return 0
            if mark[i][j] == '↖':
                self.sequence += A[i-1]
                find_sequence(mark, i - 1, j - 1)
            elif mark[i][j] == '↑':
                find_sequence(mark, i - 1, j)
            else:
                find_sequence(mark, i, j - 1)

        self.sequence = ''
        find_sequence(mark, length_A - 1, length_B - 1)
        print('DP_MEMO:')
        printf(DP)
        print('MARK_MEMO:')
        printf(mark)
        print('The Longest Common Sequence:', self.sequence[::-1], '\nLength:', len(self.sequence))
        print('Algorithm has cost {}s'.format(time.time() - start))


if __name__ == '__main__':
    # Solution().findLength(
    #     ['A', 'B', 'C', 'B', 'D', 'A', 'B'],
    #     ['B', 'D', 'C', 'A', 'B', 'A']
    # )
    # Solution().findLength(
    #     ['a', 'b', 'c', 'b', 'd', 'a', 'b'],
    #     ['b', 'd', 'c', 'a', 'b', 'a']
    # )
    Solution().findLength(
        ['a'] * 10,
        ['a'] * 10
    )
    Solution().findLength(
        ['a'] * 5,
        ['a'] * 5
    )

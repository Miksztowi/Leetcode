# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


# 586 / 586 test cases passed.
# Status: Accepted
# Runtime: 5069 ms
# Your runtime beats 43.71 % of python submissions.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound = int(n ** (1.0 / 2))
        if n * 1.0 / bound == bound:
            return 1

        squares = [x ** 2 for x in range(bound, 0, -1)]
        f = [float('inf') for x in range(n + 1)]
        f[0] = 0
        for s in squares:
            for i in range(s, n + 1):
                f[i] = min(f[i], f[i - s] + 1)
        return f[n]


# 586 / 586 test cases passed.
# Status: Accepted
# Runtime: 1522 ms
# Your runtime beats 61.71 % of python submissions.
try:
    from queue import deque
except:
    from collections import deque


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        bound = int(n ** (1.0 / 2))
        if n * 1.0 / bound == bound:
            return 1
        squares = [x ** 2 for x in range(1, bound + 1)]
        search_q = deque(squares)
        count = 1
        while search_q:
            count += 1
            size = len(search_q)
            for i in range(size):
                search_ele = search_q.popleft()
                for s in squares:
                    tmp = search_ele + s
                    if tmp == n:
                        return count
                    elif tmp < n:
                        search_q.append(tmp)
                    else:
                        break


# 586 / 586 test cases passed.
# Status: Accepted
# Runtime: 5212 ms
# Your runtime beats 42.13 % of python submissions.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0]
        while len(ans) <= n:
            cnt_perfect_squares = float('inf')
            cur_length = len(ans)
            for i in range(1, int(cur_length ** (1.0 / 2)) + 1):
                cnt_perfect_squares = min(cnt_perfect_squares, ans[cur_length - i * i] + 1)
            ans += cnt_perfect_squares,
        return ans[n]


if __name__ == '__main__':
    print(Solution().numSquares(4))

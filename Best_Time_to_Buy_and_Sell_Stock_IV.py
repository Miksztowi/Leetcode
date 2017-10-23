# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit = 0
        profit_memo = [0] * len(prices)
        for i in range(1, k+1): # When k = 1000000000, got MemoryError.
            tmp_max = profit_memo[0] - prices[0]
            for x in range(1, len(prices)):
                profit_memo[x] = max(profit_memo[x-1], tmp_max + prices[x])
                tmp_max = max(tmp_max, profit_memo[x] - prices[x])
                max_profit = max(max_profit, profit_memo[x])

        return max_profit


# 211 / 211 test cases passed.
# Status: Accepted
# Runtime: 105 ms
# Your runtime beats 68.92 % of python submissions.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # Use quickSolve() to handle the MLE and TLE.
        def quickSolve(prices):
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        if k > len(prices)/2:
            return quickSolve(prices)

        k = min(len(prices) / 2, k)  # Optimize the parameters.

        profit_memo = [[0] * len(prices) for _ in range(k+1)]
        for i in range(1, k+1): # When k = 1000000000, got MemoryError.
            tmp_max = profit_memo[i-1][0] - prices[0]
            for x in range(1, len(prices)):
                profit_memo[i][x] = max(profit_memo[i][x-1], tmp_max + prices[x])
                tmp_max = max(tmp_max, profit_memo[i-1][x] - prices[x])

        return profit_memo[k][-1]


# Here is the fastest solution in leetcode.
# Only cost 55ms. That's half of my solution.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        if k >= len(prices) / 2:
            result = 0
            current = -prices[0]
            for ii in range(1, len(prices)):
                if prices[ii] < prices[ii - 1]:
                    result += current + prices[ii - 1]
                    current = -prices[ii]
            return result + current + prices[-1]

        k = min(len(prices) / 2, k)

        if k == 0:
            return 0
        no_have = [0 for ii in range(k + 1)]
        have = [-prices[0] for ii in range(k + 1)]
        for ii in range(1, len(prices)):
            if prices[ii] > prices[ii - 1]:
                for jj in range(k, 0, -1):
                    tmp = have[jj] + prices[ii]
                    if tmp <= no_have[jj]:
                        break
                    else:
                        no_have[jj] = tmp
            elif prices[ii] < prices[ii - 1]:
                for jj in range(k, 0, -1):
                    tmp = no_have[jj - 1] - prices[ii]
                    if tmp <= have[jj]:
                        break
                    else:
                        have[jj] = tmp

        return no_have[-1]

if __name__ == '__main__':
    print(Solution().maxProfit(2, [1, 3, 7, 5, 10, 3]))
    print(Solution().maxProfit(2, [3,3,5,0,0,3,1,4]))
    print(Solution().maxProfit(1, [1]))
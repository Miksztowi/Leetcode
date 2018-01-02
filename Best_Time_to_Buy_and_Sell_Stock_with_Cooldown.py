# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]
# Credits:
# Special thanks to @dietpepsi for adding this problem and creating all test cases.


# 211 / 211 test cases passed.
# Status: Accepted
# Runtime: 39 ms
# Your runtime beats 51.59 % of python submissions.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)


# 211 / 211 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Your runtime beats 17.20 % of python submissions.
# DP Formula:
# Buy[x] = max(Buy[x-1], Sell[x-2] - p).
# Sell[x] = max(Sell[x-1], Buy[x-1] + p).
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        pre_sell, buy, pre_buy, sell = 0, -prices[0], 0, 0
        for p in prices:
            pre_buy = buy
            buy = max(pre_sell - p, pre_buy)
            pre_sell = sell
            sell = max(sell, pre_buy + p)
        return sell


if __name__ == '__main__':
    print(Solution().maxProfit([1, 2, 3, 0, 2]))
    print(Solution().maxProfit([2, 1, 3, 0, 2]))

# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


# 198 / 198 test cases passed.
# Status: Accepted
# Runtime: 42 ms
# Your runtime beats 52.33 % of python submissions.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sold, bought = 0, float('-inf')
        for p in prices:
            sold = max(sold, bought + p)
            bought = max(bought, sold - p)
        return sold if sold > 0 else 0


if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9]))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3]))



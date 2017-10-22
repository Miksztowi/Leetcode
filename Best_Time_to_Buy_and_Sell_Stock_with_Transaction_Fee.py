# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Your are given an array of integers prices,
# for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
# You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.


# DP formula:  sold = max(sold, bought + cur_price - fee) if sell stock is the best choice or continue holding the stock
#              bought = max(bought, sold - cur_price)  Buy the new stock if after that the money still more than begin.
# Time complexity: O(n)
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        sold, bought = 0, float("-inf")
        for p in prices:
            sold = max(sold, bought + p - fee)
            bought = max(bought, sold - p)
        return sold if sold > 0 else 0



if __name__ == '__main__':
    # print(Solution().maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3], 3))

# 44 / 44 test cases passed.
# Status: Accepted
# Runtime: 275 ms

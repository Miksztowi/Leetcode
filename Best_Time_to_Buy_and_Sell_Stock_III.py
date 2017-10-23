# -*- encoding:utf-8 -*-
# __author__=='Gan'


# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# DP formula:
# F(x) = max(F(x-1), M(x-1) + prices[i])  k is transaction times.
# M(x) = max(M(x-1), profit_memo[k-1][x] - prices[i]).
# 198 / 198 test cases passed.
# Status: Accepted
# Runtime: 118 ms
# Your runtime beats 12.48 % of python submissions.
# Time Complexity: O(n), actually is kn
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        transaction_times = 2
        max_profit = 0
        profit_memo = [[0] * len(prices) for x in range(transaction_times+1)]
        for k in range(1, transaction_times+1):
            tmp_max = profit_memo[k-1][0] - prices[0]
            for i in range(1, len(prices)):
                profit_memo[k][i] = max(profit_memo[k][i-1], tmp_max+prices[i])
                tmp_max = max(tmp_max, profit_memo[k-1][i] - prices[i])
                max_profit = max(max_profit, profit_memo[k][i])
        return max_profit


# 198 / 198 test cases passed.
# Status: Accepted
# Runtime: 48 ms
# Your runtime beats 97.74 % of python submissions.
# Time Complexity: O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        first_sold = second_sold = 0
        first_bought = second_bought = float('-inf')
        for p in prices:
            second_sold = max(second_sold, second_bought + p)
            second_bought = max(second_bought, first_sold - p)
            first_sold = max(first_sold, first_bought + p)
            first_bought = max(first_bought, -p)

        return second_sold if second_sold > 0 else 0

# Although this solution is not concise, but for the understanding is very helpful.
# Use DP formula that only allow transactions once from left to right and from right to left.
# After getting two memo lists, iterate to find the optimal answer.
# 198 / 198 test cases passed.
# Status: Accepted
# Runtime: 379 ms
# Your runtime beats 1.05 % of python submissions.
class Solution():
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        min_price, max_profit_from_left, max_profits_from_left = float("inf"), 0, []
        for price in prices:
            min_price = min(min_price, price)
            max_profit_from_left = max(max_profit_from_left, price - min_price)
            max_profits_from_left.append(max_profit_from_left)

        max_price, max_profit_from_right, max_profits_from_right = 0, 0, []
        for i in reversed(range(len(prices))):
            max_price = max(max_price, prices[i])
            max_profit_from_right = max(max_profit_from_right, max_price - prices[i])
            max_profits_from_right.insert(0, max_profit_from_right)

        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_profits_from_left[i] + max_profits_from_right[i])

        print(max_profits_from_left, max_profits_from_right)

        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([1, 3, 2, 8, 4, 9]))
    print(Solution().maxProfit([1, 3, 7, 5, 10, 3]))
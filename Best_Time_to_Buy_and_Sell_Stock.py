# -*- encoding:utf-8 -*-
# __author__=='Gan'

# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# In this case, no transaction is done, i.e. max profit = 0.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        lo, hi = 0, len(prices)
        max_profit = 0
        interval = 1
        while lo + interval < hi:
            if prices[lo + interval] > prices[lo]:
                max_profit = max(max_profit, prices[lo + interval] - prices[lo])
                interval += 1
            else:
                lo += interval
                interval = 1
        return max_profit


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([2, 4, 1]))
    print(Solution().maxProfit([]))


# Here are some solutions to understand more easier than mine.

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        max_profit, min_price = 0, float("inf")
        # float("inf") means positive infinity
        # float("-inf") means negative infinity
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0
        curMin = prices[0]
        curMax = prices[0]
        curDif = 0
        for p in prices:
            if p < curMin:
                curMin = p
                curMax = p
            if p > curMax:
                curMax = p
                curDif = max(curDif, curMax - curMin)

        return curDif

# ##！！！！！！！ So important
# The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm.
        #  Since no body has mentioned this so far, I thought it's a good thing for everybody to know.
#
# All the straight forward solution should work,
        #  but if the interviewer twists the question slightly by giving the difference array of prices,
        # Ex: for {1, 7, 4, 11}, if he gives {0, 6, -3, 7}, you might end up being confused.
# Here, the logic is to calculate the difference (maxCur += prices[i] - prices[i-1]) of the original array,
        #  and find a contiguous subarray giving maximum profit. If the difference falls below 0, reset it to zero.
    # public int maxProfit(int[] prices) {
    #     int maxCur = 0, maxSoFar = 0;
    #     for(int i = 1; i < prices.length; i++) {
    #         maxCur = Math.max(0, maxCur += prices[i] - prices[i-1]);
        # if p[i-1] < 0, it will be reset zero in next calculate.
    #         maxSoFar = Math.max(maxCur, maxSoFar);
    #     }
    #     return maxSoFar;
    # }
'''
Given an array which its elements are the prices,
With one transaction, find the max profit of a trade

Example:
input: [7, 1, 5, 3, 6, 4]
output: 5

Explanation: Buy on day 2 (1), sell on day 5 (6), with profit = 6 - 1 = 5
'''


class Solution:
    def maxProfit(self, prices, list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while l < r:
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1

        return maxP

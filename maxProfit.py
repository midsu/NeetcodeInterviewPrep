


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

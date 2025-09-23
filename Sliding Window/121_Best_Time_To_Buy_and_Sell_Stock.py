"""
121. Best Time to Buy and Sell Stock
Level: Easy
Topics: Array, Dynamic Programming
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        holdPrice = float("inf")
        for price in prices:
            if price < holdPrice:
                holdPrice = price 
            currProfit = price - holdPrice
            res = max(res, currProfit)
        return res 
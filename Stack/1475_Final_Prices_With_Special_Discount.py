"""
1475. Final Prices With a Special Discount in a Shop
Level: Easy 
Topics: Array, Stack, Monotonic Stack
Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop?envType=problem-list-v2&envId=stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        priceStack = []
        res = prices
        for index, price in enumerate(prices):
            while priceStack and price <= priceStack[-1][1]:
                idx, p = priceStack.pop()
                res[idx] = p - price
            priceStack.append((index, price))
        return res
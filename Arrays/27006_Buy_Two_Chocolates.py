"""
27006. Buy Two Chocolates
Level: Easy
Topics: Array, Sorting, Greedy
Link: https://leetcode.com/problems/buy-two-chocolates?envType=problem-list-v2&envId=sorting
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices.sort()
        cost = prices[0] + prices[1]
        if cost <= money:
            return money - cost 
        else:
            return money 
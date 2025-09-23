"""
875. Koko Eating Bananas
Level: Medium
Topics: Arrays, Binary Search
Link: 
Time Complexity: O(n log m); n -number of piles and m - maximum number of bananas in a pile
Space Complexity: O(1)
"""


import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxPiles = max(piles)
        low, high = 1, maxPiles
        res = high 
        while low <= high:
            rate = low + (high - low) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / rate)
            if hours <= h:
                res = rate 
                high = rate - 1
            else:
                low = rate + 1
        return res
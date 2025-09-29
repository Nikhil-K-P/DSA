"""
441. Arranging Coins
Level: Easy
Topics: Binary Search, Math
Link: https://leetcode.com/problems/arranging-coins?envType=problem-list-v2&envId=binary-search
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n 
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            Sum = m * (m + 1) // 2
            if Sum <= n:
                res = m 
                l = m + 1
            else:
                r = m - 1
        return res 
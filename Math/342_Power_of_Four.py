"""
342. Power of Four
Level: Easy
Topics: Math, Bit Manipulation
Link: https://leetcode.com/problems/power-of-four?envType=problem-list-v2&envId=math
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False 
        while n % 4 == 0:
            n = n // 4
        return n == 1
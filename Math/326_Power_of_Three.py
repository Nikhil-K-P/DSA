"""
326. Power of Three
Level: Easy
Topics: Math, Recursion
Link: https://leetcode.com/problems/power-of-three?envType=problem-list-v2&envId=math
Time Complexion: O(log n)
Space Complexion: O(1)
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1
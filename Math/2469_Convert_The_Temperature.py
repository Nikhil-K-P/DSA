"""
2469. Convert the Temperature
Level: Easy
Topics: Math
Link: https://leetcode.com/problems/convert-the-temperature?envType=problem-list-v2&envId=math
Time Complexion: O(1)
Space Complexion: O(1)
"""


class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
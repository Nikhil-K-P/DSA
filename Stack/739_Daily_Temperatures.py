"""
739. Daily Temperatures
Level: Medium
Topics: Stack, Array, Monotonic Stack
Link: 
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                lastTemp, lastIndex = stack.pop() 
                res[lastIndex] = idx - lastIndex
            stack.append((temp,idx))
        return res
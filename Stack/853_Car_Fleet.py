"""
853. Car Fleet
Level: Medium 
Topics: Array, Stack, Sorting, Monotonic Stack
Link: https://leetcode.com/problems/car-fleet
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        carMap = [(pos, speed) for pos, speed in zip(position, speed)]
        carMap.sort(reverse = True)
        stack = []
        for pos, speed in carMap:
            time = (target - pos) / speed 
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)
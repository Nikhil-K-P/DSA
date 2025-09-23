"""
11. Container With Most Water
Level: Medium
Topics: Array, Two Pointers, Greedy
Link: https://leetcode.com/problems/container-with-most-water
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = 0
        while left <= right:
            area = min(height[left], height[right]) * (right - left)
            res = max(res, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return res
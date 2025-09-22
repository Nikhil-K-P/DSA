"""
704. Binary Search
Level: Easy
Topics: Array, Binary Search
Link: https://leetcode.com/problems/binary-search
Time Complexity: O(log n)
Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                start = mid + 1
            else: 
                end = mid - 1
        return -1 
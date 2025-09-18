"""
747. Largest Number At Least Twice of Others
Level: Easy
Topics: Array, Math
Link: https://leetcode.com/problems/largest-number-at-least-twice-of-others?envType=problem-list-v2&envId=sorting
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = float("-inf")
        largestIdx = 0
        secondLargest = float("-inf")
        for idx, n in enumerate(nums):
            if n > largest:
                secondLargest = largest
                largest = n
                largestIdx = idx
            elif n > secondLargest:
                secondLargest = n
        if largest // 2 >= secondLargest:
            return largestIdx
        return -1 
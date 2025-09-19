"""
128. Longest Consecutive Sequence
Level: Medium
Topics: Array, Hash Table, Union Find
Link: https://leetcode.com/problems/longest-consecutive-sequence
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet: 
                    length += 1
                res = max(res, length)
        return res
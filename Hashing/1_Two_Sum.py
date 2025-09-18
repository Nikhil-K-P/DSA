"""
1. Two Sum
Level: Easy
Topics: Array, Hash Table
Link: https://leetcode.com/problems/two-sum
Time COmplexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = [0] * 2
        indexMap = {}
        for idx, n in enumerate(nums):
            find = target - n
            if find in indexMap:
                res[0], res[1] = indexMap[find], idx
                break
            indexMap[n] = idx
        return res
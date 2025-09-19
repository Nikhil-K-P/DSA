"""
238. Product of Array Except Self
Level: Medium
Topics: Array, Prefix Sum
Link: https://leetcode.com/problems/product-of-array-except-self
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        suffix = 1 
        for i in range(n - 1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]
        return prefix 
"""
905. Sort Array By Parity
Level: Easy
Topics: Array, Two Pointers, Sorting
Link: https://leetcode.com/problems/sort-array-by-parity?envType=problem-list-v2&envId=sorting
Time Complexion: O(n)
Space Complexion: O(n)
Follow up: you solve this problem in-place
"""


class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []
        i = j = 0 
        while i < n:
            if nums[i] % 2 == 0:
                res.append(nums[i])
            i += 1
        while j < n:
            if nums[j] % 2 != 0:
                res.append(nums[j])
            j += 1
        return res
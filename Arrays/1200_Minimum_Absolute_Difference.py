"""
1200. Minimum Absolute Difference
Level: Easy
Topics: Arrays, Sorting
Link: https://leetcode.com/problems/minimum-absolute-difference?envType=problem-list-v2&envId=sorting
Time Complexion: O(n log n)
Space Complexion: O(1)
"""


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        res = []
        arr.sort()
        n = len(arr)
        minDiff = float('inf')
        for i in range(n - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff == minDiff:
                res.append([arr[i], arr[i + 1]])
        return res
"""
1356. Sort Integers by The Number of 1 Bits
Level: Easy
Topics: Array, Bit Manipulation, Sorting, Counting
Link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits?envType=problem-list-v2&envId=counting
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from collections import heapq

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        res = []
        heap = []
        for num in arr:
            count = 0
            n = num
            while num:
                num &= num - 1
                count += 1
            heapq.heappush(heap, (count, n))
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res
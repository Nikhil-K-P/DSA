"""
973. K Closest Points to Origin
Level: Medium
Topics: Array, Divide and Conquer, Math, Geometry, Sorting, Heap (Priority Queue), Quickselect
"""

from collections import heapq
import math


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        res = []
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (- distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

"""
2500. Delete Greatest Value in Each Row
Level: Medium
Topics: Array, Matrix, Sorting, Heap (Priority Queue)
Link: https://leetcode.com/problems/delete-greatest-value-in-each-row?envType=problem-list-v2&envId=heap-priority-queue
Time Complexity: O(m * n log n)
Space Complexity: O(1)
"""

from collections import heapq
class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            heapq.heapify(grid[i])
        for i in range(n):
            num = 0
            for i in range(m):
                num = max(num, heapq.heappop(grid[i]))
            res += num
        return res 
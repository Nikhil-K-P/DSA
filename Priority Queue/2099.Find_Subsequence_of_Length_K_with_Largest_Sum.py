"""
2099. Find Subsequence of Length K with the Largest Sum
Level: Easy
Topics: Array, Heap (Priority Queue), Sorting
Link: https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum?envType=problem-list-v2&envId=heap-priority-queue
Notes: Can also be solved using Sorting
Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))
            if len(heap) > k:
                heapq.heappop(heap)
        
        heap.sort(key=lambda x: x[1])
        return [n for n, i in heap]
"""
1046. Last Stone Weight
Level: Easy
Topics: Array, Heap (Priority Queue), Sorting
Link: https://leetcode.com/problems/relative-ranks
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -weight)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        
        return -heap[0] if heap else 0
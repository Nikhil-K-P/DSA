"""
1464. Maximum Product of Two Elements in an Array
Level: Easy
Topics: Array, Heap (Priority Queue), Sorting
Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array?envType=problem-list-v2&envId=heap-priority-queue
Notes: Can also be solved using 
Approach 1: Sorting 
Approach 2: One pass to find two largest number 
Time Complexity: O(n)
Space Complexity: O(1)
"""
import heapq

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > 2:
                heapq.heappop(heap)
        x = heap[0] - 1
        y = heap[1] - 1
        return x * y
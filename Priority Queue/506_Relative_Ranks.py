"""
506. Relative Ranks
Level: Easy
Topics: Array, Hash Table, Sorting, Heap (Priority Queue)
Link: https://leetcode.com/problems/relative-ranks
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
import heapq

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n = len(score)
        res = [""] * n 
        heap = []
        for i, s in enumerate(score):
            heapq.heappush(heap, (-s, i))
        pos = 1
        while heap:
            s, i = heapq.heappop(heap)
            print(i, s)
            if pos == 1:
                res[i] = "Gold Medal"
            elif pos == 2:
                res[i] = "Silver Medal"
            elif pos == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = str(pos)
            pos += 1
        return res 
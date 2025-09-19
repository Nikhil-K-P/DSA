"""
692. Top K Frequent Words
Level: Medium
Topics: Hash Table, String, Heap (Priority Queue)
Link: https://leetcode.com/problems/top-k-frequent-words?envType=problem-list-v2&envId=heap-priority-queue
Time Complexity: O(n log k)  n - number of unique words
Space Complexity: O(n) N - number of unique words.
"""


import functools
import heapq
@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = {}
        heap = []
        for s in words:
            count[s] = 1 + count.get(s, 0)
        for word, cnt in count.items():
            heapq.heappush(heap, (Element(cnt, word), word))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]
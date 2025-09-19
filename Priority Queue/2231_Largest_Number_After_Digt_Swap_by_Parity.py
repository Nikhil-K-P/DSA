"""
2231. Largest Number After Digit Swaps by Parity
Level: Easy 
Topic: Sorting, Priority Queue
Link: https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity?envType=problem-list-v2&envId=heap-priority-queue
Time Complexity: O(n log n)
Space Complexity: O(n)
"""
from collections import heapq

class Solution:
    def largestInteger(self, num: int) -> int:
        even = []
        odd = []
        n = num 
        res = 0
        while n:
            rem = n % 10 
            if rem % 2 == 0:
                heapq.heappush(even, -rem)
            else:
                heapq.heappush(odd, -rem)
            n = n // 10
        number = str(num)
        for n in number:
            res *= 10
            if int(n) % 2 == 0:
                res += -heapq.heappop(even)
            else:
                res += -heapq.heappop(odd)
        return res 
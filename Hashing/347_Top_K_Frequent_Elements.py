"""
347. Top K Frequent Elements
Level: Medium
Topics: Array, Hash Table, Sorting, Heap (Priority Queue), Bucket Sort, Counting
Link: https://leetcode.com/problems/top-k-frequent-elements
Time Complexity: O(n)
Space Complexity: O(n)
Alternative Approach:
Using Heap (Priority Queue) and once the len of the heap exceeds k, pop the smallest element.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        count = [[] for i in range(n + 1)]
        frequency = {}
        res = []

        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)

        for key, value in frequency.items():
            count[value].append(key)

        m = len(count)
        for i in range(m - 1, -1, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
"""
1539. Kth Missing Positive Number
Level: Easy
Topic: Hash Table, Array, Binary Search
Link: https://leetcode.com/problems/kth-missing-positive-number
Time Complexity: O(n + k) n - no of elements in arr
Space Complexity: O(n)
Note: This can also be solved using Binary Search with O(log n) time complexity. 
The binary search option is given below 
"""


class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        n = arr[-1]
        res = 0
        missingCount = 0
        numSet = set(arr)
        for i in range(1, n + k + 1):
            if i not in numSet:
                missingCount += 1
                if missingCount == k:
                    res = i 
                    break 
        return res 
    

    def findKthPositiveBinarySearch(self, arr: list[int], k: int) -> int:
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                beg = mid + 1
            else:
                end = mid
        return end + k
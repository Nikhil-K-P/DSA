"""
2053. Kth Distinct String in an Array
Level: Easy
Topics: Array, Hash Table, String, Counting
Link: https://leetcode.com/problems/kth-distinct-string-in-an-array?envType=problem-list-v2&envId=hash-table
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        res = ''
        count = {}
        for s in arr:
            count[s] = 1 + count.get(s, 0)
        for s in arr:
            if count[s] == 1:
                r = s
                k -= 1
                if k == 0:
                    res = r
                    break 
        return res
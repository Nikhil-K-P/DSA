"""
981. Time Based Key-Value Store
Level: Medium
Topics: Hash Table, String, Binary Search, Design
Link: https://leetcode.com/problems/time-based-key-value-store
Time Complexity: O(log n) for get, O(1) for set
Space Complexity: O(n)
"""


from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.timeMap[key])
        values = self.timeMap[key]
        res = ""
        start, end = 0, n - 1
        while start <= end:
            mid = start + (end - start) // 2
            time, value = values[mid]
            if time == timestamp:
                return value
            elif time < timestamp:
                start = mid + 1
                res = value
            else:
                end = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
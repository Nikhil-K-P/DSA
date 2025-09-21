"""
3508. Implement Router
Level: Medium 
Topics: Array, Design, Hash Table, Binary Search, Queue, Ordered Set
Link: https://leetcode.com/problems/implement-router?envType=daily-question&envId=2025-09-20
Time Complexity: O(1) for addPacket and forwardPacket, O(log n) for getCount
Space Complexity: O(m) where m is the memory limit of the router
"""

from bisect import bisect
from collections import deque, defaultdict

class Router:

    def __init__(self, memoryLimit: int):
        self.deque = deque()
        self.memoryLimit = memoryLimit
        self.packets = set()
        self.destinationMap = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packets:
            return False

        if len(self.deque) >= self.memoryLimit:
            removedPacket = self.deque.popleft()
            self.packets.remove(removedPacket)
            self.destinationMap[removedPacket[1]].pop(0)

        self.deque.append(packet)
        self.packets.add(packet)
        self.destinationMap[destination].append(timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.deque:
            return []

        packet = self.deque.popleft()
        self.packets.remove(packet)
        self.destinationMap[packet[1]].pop(0)
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timeStamp = self.destinationMap[destination]
        lastIndex = bisect.bisect_right(timeStamp, endTime)
        firstIndex = bisect.bisect_left(timeStamp, startTime)
        return lastIndex - firstIndex
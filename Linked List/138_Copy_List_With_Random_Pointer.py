"""
138. Copy List with Random Pointer
Level: Medium
Topics: Hash Table, Linked List
Link: 
Time Complexion: O(n)
Space Complexion: O(n)
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeMap = {None: None}
        curr = head 
        while curr: 
            newNode = Node(curr.val)
            nodeMap[curr] = newNode
            curr = curr.next 
        curr = head
        while curr:
            newNode = nodeMap[curr]
            oldNext, oldRandom = curr.next, curr.random
            newNext, newRandom = nodeMap.get(oldNext, None), nodeMap.get(oldRandom, None)
            newNode.next, newNode.random = newNext, newRandom
            curr = curr.next 
        return nodeMap[head]
"""
141. Linked List Cycle
Level: Easy
Topic: Hash Table, Linked List, Two Pointers
Link: https://leetcode.com/problems/linked-list-cycle
Time Complexity: O(n) n - no of nodes in LL
Space Complexity: O(1)
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True 
        return False
"""
19. Remove Nth Node From End of List
Level: Medium
Topic: Linked List, Two Pointers
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list
Time Complexity: O(n) n - no of nodes in LL
Space Complexity: O(1)
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left, right = dummy, head
        while right and n : 
            right = right.next 
            n -= 1

        while right:
            left = left.next 
            right = right.next

        left.next = left.next.next
        return dummy.next
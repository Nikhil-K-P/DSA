"""
143. Reorder List
Level: Medium
Topic: Linked List, Two Pointers, Stack, Recursion
Link: 
Time Complexity: O(n) n - no of nodes in LL
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None 
        while curr:
            temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = temp
        reverse = prev
        res = head
        while head and reverse:
            temp1 = head.next
            head.next = reverse 
            temp2 = reverse.next
            reverse.next = temp1
            reverse = temp2
            head = temp1
        return res 

            
        
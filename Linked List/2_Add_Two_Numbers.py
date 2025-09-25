"""
2. Add Two Numbers
Level: Medium
Topic: Linked List, Math, Recursion
Link: 
Time Complexity: O(max(m, n)) m - no of nodes in l1, n - no of nodes in l2
Space Complexity: O(max(m, n))
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = prev = ListNode()
        while l1 and l2:
            add = (l1.val + l2.val + carry) 
            rem = add % 10 
            carry = add // 10 
            node = ListNode(rem, None)
            prev.next = node 
            prev = prev.next 
            l1, l2 = l1.next, l2.next
        while l1: 
            add = (l1.val + carry) 
            rem = add % 10 
            carry = add // 10 
            node = ListNode(rem, None)
            prev.next = node 
            prev = prev.next 
            l1 = l1.next
        while l2: 
            add = (l2.val + carry) 
            rem = add % 10 
            carry = add // 10 
            node = ListNode(rem, None)
            prev.next = node 
            prev = prev.next 
            l2 = l2.next
        if carry:
            node = ListNode(carry, None)
            prev.next = node
        return head.next
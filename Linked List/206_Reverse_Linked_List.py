"""
206. Reverse Linked List
Level: Easy
Topic: Linked List, Recursion
Link: https://leetcode.com/problems/reverse-linked-list
Time Complexity: O(n) n - no of nodes in LL
Space Complexity: O(1)
"""


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 
        return prev
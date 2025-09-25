"""
21. Merge Two Sorted Lists
Level: Easy
Topic: Linked List, Recursion
Link: https://leetcode.com/problems/merge-two-sorted-lists
Time Complexity: O(n + m) n - no of nodes in list1, m - no of nodes in list2
Space Complexity: O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode() 
        head = res
        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next 
            else:
                res.next = list2
                list2 = list2.next 
            res = res.next
        res.next = list1 or list2
        return head.next
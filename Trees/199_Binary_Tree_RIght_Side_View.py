"""
199. Binary Tree Right Side View
Level: Medium
Topic: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: https://leetcode.com/problems/binary-tree-right-side-view
Time Complexity: O(n)
Space Complexity: O(n)
"""


import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
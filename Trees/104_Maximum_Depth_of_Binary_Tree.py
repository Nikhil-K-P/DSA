"""
104. Maximum Depth of Binary Tree
Level: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Link: 
Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
"""
572. Subtree of Another Tree
Level: Easy
Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree, Hash Function, String Matching
Link : https://leetcode.com/problems/subtree-of-another-tree
Time Complexity: O(m * n)
Space Complexity: O(m + n)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True 
        if p and q and p.val == q.val:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False
        if not root and not subRoot: 
            return True

        if self.isSameTree(root, subRoot):
            return True 

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right
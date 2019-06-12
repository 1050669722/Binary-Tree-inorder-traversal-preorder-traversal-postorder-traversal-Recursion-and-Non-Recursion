# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 14:33:08 2019

@author: Administrator
"""

'''

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        ans = []
        ans.append(root.val)
        ans += self.preorderTraversal(root.left)
        ans += self.preorderTraversal(root.right)
        return ans

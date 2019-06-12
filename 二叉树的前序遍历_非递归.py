# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:04:56 2019

@author: Administrator
"""

'''
Binary Tree | Preorder Traversal | Non-Recursion
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        current = root
        stack = []
        ans = []
        while current or stack:
            if current:
                stack.append(current)
                ans.append(current.val)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        return ans
    


















    

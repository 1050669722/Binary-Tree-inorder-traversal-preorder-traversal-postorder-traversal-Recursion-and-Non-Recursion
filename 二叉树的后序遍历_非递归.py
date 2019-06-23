# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:04:56 2019

@author: Administrator
"""

'''
Binary Tree | Postorder Traversal | Non-Recursion
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        current = root
        stack = []
        last_visit = root
        ans = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack[-1]
            if not current.right or current.right == last_visit:
                ans.append(current.val)
                last_visit = current
                stack.pop()
                current = None
            else:
                current = current.right
        return ans
    

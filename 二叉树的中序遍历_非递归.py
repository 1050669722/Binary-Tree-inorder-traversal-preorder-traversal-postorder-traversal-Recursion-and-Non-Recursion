# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:04:56 2019

@author: Administrator
"""

'''
Binary Tree | Inorder Traversal | Non-Recursion
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:        
#        current = root
#        stack = []
#        ans = []
#        while current or stack:
#            if current:
#                stack.append(current) #存入栈
#                current = current.left #向左移
#            else:
#                current = stack.pop() #弹出栈
#                ans.append(current.val)
#                current = current.right #向右移
#        return ans
    
        current = root
        stack = []
        ans = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                ans.append(current.val)
                current = current.right
        return ans
    
    
    
    
    

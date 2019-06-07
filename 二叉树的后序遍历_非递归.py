# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:04:56 2019

@author: Administrator
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
#        current = root
#        stack = []
#        ans = []
#        last_visit = root
#        while current or stack:
#            while current: #一直进栈，一直左移
#                stack.append(current)
#                current = current.left
#            current = stack[-1] #退回到最后一个结点
#            if (not current.right) or current.right == last_visit: #如果右子树不存在 或者 右子树是上一个看过的结点
#                ans.append(current.val)
#                last_visit = current
#                stack.pop()
#                current = None #要回到某一步，这是后序遍历不同之处
#            else:
#                current = current.right #再一次，把右结点当做这一层原先的根结点
#        return ans
    
    
        current = root
        stack = []
        last_visit = root
        ans =[]
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
    


















    
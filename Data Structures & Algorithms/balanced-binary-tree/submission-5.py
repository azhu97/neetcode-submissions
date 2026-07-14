# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        b = True

        def rec(node):
            nonlocal b  # this is needed to update outer 'b'
            if node == None:
                return -1
            
            left = rec(node.left)
            right = rec(node.right)
            
            if abs(left - right) > 1:
                b = False

            return max(left, right) + 1
        
        rec(root)
        return b
        
            


        
        
        
        
        
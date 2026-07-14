# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preorder(node):
            if not node:
                return ""
            res = [] 
            stack = [node]
            while stack:
                # the same as recursion 
                # replicates a dfs' greed
                temp = stack.pop()
                res.append(temp.val)
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
            return ("".join(str(x) for x in res))
        
        return (preorder(subRoot) in preorder(root))
        
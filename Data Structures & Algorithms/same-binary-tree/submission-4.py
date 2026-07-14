# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def dfs(root1, root2):
            print(root1, root2)
            nonlocal same
            if root1 == root2 == None:
                print(1)
                return 
            if root1 and not root2 or root2 and not root1 or root1.val != root2.val:
                print(2)
                same = False
                return
            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

        dfs(p, q)
        return same
            
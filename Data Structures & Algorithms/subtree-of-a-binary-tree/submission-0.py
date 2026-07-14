# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.dfs(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def dfs(self, node1, node2):
        # cases where we know match on this end
        if node1 is None and node2 is None:
            return True
        if (node1 is None and node2) or (node1 and node2 is None) or (node1.val != node2.val):
            return False
        return self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)
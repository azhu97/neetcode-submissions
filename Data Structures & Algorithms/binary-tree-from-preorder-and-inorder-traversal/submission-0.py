# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {} # given inorder nodes, maps node -> index
        for i, val in enumerate(inorder):
            mapping[val] = i
        
        pre_index = 0
        def helper(left, right):
            nonlocal pre_index
            if left > right:
                return None

            root_val = preorder[pre_index]
            pre_index += 1
            mid = mapping[root_val]
            root = TreeNode(val=root_val)
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(preorder) - 1)


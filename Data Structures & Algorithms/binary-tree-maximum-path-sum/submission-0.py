# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# path in a binary tree is the sequence of adjacent nodes with a connecting edge 
# node cannot appear more than once in the sequence more than once 
# doesn't need to include the root
# find the max sum of all the values, note that this is not a binary tree 
# sort of like a dp problem, we want to go all the the way down left, then all the way down right
# then we have a conclusion
# max(left, right, mid, left + mid, right + mid, left + mid + right)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node is None:
                return float('-inf')
            
            mid = node.val
            left, right = helper(node.left), helper(node.right)
            print(left, mid, right)
            return max(left, right, mid, left + mid, mid + right, left + mid + right)
        
        return helper(root)
            
        
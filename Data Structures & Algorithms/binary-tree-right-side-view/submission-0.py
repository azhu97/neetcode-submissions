# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = set()
        # run bfs with priority to the right 
        def dfs(root, floor):
            # nonlocal res
            # nonlocal level
            if not root:

                return 
            if floor not in level:
                res.append(root.val)
                level.add(floor)
            dfs(root.right, floor + 1)
            dfs(root.left, floor + 1)

        dfs(root, 0)
        print(res)
        print(level)
        return res
            
            

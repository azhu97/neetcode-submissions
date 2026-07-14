# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = deque([root])
        def bfs(que):
            while que:
                repeat = len(que)
                temp_arr = []
                for i in range(repeat):
                    node = que.popleft()
                    temp_arr.append(node.val)
                    if node.left:
                        que.append(node.left)
                    if node.right:
                        que.append(node.right)
                res.append(temp_arr.copy())
        bfs(que)
        return res


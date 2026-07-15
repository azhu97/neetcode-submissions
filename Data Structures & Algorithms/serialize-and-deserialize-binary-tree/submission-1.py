# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return "N"
        res = []
        que = deque([root])
        while que:
            temp = que.popleft()
            if temp is None:
                res.append('N')
            else:
                res.append(str(temp.val))
                if temp.left:
                    que.append(temp.left)
                else:
                    que.append(None)
                if temp.right:
                    que.append(temp.right)
                else:
                    que.append(None)
            res.append('#')
            
        res.pop()
        res = "".join(res)
        return res
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        temp = data.split("#")
        res = []
        for node in temp:
            if node == 'N':
                res.append(None)
            else:
                res.append(TreeNode(int(node)))
        i = 1
        for node in res:
            print(i)
            if node is None:
                continue
            if i < len(res):
                node.left = res[i]
                i += 1
            if i < len(res):
                node.right = res[i]
                i += 1
        return res[0]
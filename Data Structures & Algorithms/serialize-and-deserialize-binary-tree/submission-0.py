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
            
        print(res)
        res.pop()
        res = "".join(res)
        return res
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        if len(data) == 1:
            return None

        temp = data.split("#")
        res = []
        for x in temp:
            if x == 'N':
                res.append(None)
            else:
                res.append(TreeNode(int(x)))
        
        print(res)
        for i, node in enumerate(res):
            print(i)
            if node is None:
                continue
            if i * 2 + 1 < len(res):
                node.left = res[i * 2 + 1]
                if res[i * 2 + 1]:
                    print(f"node {node.val} points to {res[i * 2 + 1].val}")
            if i * 2 + 2 < len(res):
                node.right = res[i * 2 + 2]
                if res[i * 2 + 2]:
                    print(f"node {node.val} points to {res[i * 2 + 2].val}")
        return res[0]
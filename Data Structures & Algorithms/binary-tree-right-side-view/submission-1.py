# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        # bfs w level counter
        result = []
        q = deque([root])

        while q:
            right = None
            n = len(q)

            for i in range(n):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                result.append(right.val)

        return result




            

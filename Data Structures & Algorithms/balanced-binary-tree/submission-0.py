# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal = True

        if root is None:
            return True

        def balance(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left_h = balance(root.left)
            right_h = balance(root.right)

            if abs(left_h - right_h) > 1:
                self.bal = False

            return 1 + max(left_h, right_h)
        
        balance(root)
        return self.bal
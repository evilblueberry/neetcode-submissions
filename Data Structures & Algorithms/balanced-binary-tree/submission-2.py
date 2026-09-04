# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if not root:
            return True

        def balance(root: Optional[TreeNode]) -> int:
            if root is None:
                return -1

            left = balance(root.left) + 1
            right = balance(root.right) + 1
            bal = abs(left - right)

            if bal > 1:
                self.balanced = False
           
            return max(left, right)
        
        
        return abs(balance(root.left) - balance(root.right)) <= 1 and self.balanced



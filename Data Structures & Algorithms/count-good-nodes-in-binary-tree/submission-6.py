# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        largest = root.val

        def gnodes(root: TreeNode, largest) -> int:
            if root is None:
                return 0

            curr_count = 0

            if root.val >= largest:
                largest = root.val
                curr_count += 1

           
            left = gnodes(root.left, largest)
            right = gnodes(root.right, largest)

            return left + right + curr_count

        count = gnodes(root, largest)
        return count




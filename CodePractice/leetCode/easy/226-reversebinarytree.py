# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# def reverse(self):
#     self.left, self.right = self.right, self.left
#     if self.left != None:
#         self.left.reverse()
#     if self.right != None:
#         self.right.reverse()
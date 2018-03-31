# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or not root.left:
            return root
        newroot=self.upsideDownBinaryTree(root.left)
        root.left.left=root.right
        root.left.right=root
        root.left=None
        root.right=None
        return newroot

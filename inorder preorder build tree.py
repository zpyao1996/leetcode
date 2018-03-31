# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        if not mid==0:
            node.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        if not mid==len(preorder)-1:
            node.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return node



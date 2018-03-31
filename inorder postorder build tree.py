import queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        left=None
        i=0
        while i<len(inorder):
            if inorder[i]==postorder[i]:
                node=TreeNode(inorder[i])
                node.left=left
                left=node
                i+=1
            else:
                rindex=postorder.index(inorder[i])
                node=TreeNode(inorder[i])
                node.left=left
                node.right=self.buildTree(inorder[i+1:rindex+1],postorder[i:rindex])
                i=rindex+1
        return node





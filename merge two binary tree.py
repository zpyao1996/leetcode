# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        root=self.mergehelper(t1,t2)
        return root
    def mergehelper(self,t1,t2,p):
        if not t1 and not t2:
            return None
        if not t1:
            p=t2
        elif not t2:
            p=t1
        else:
            p=TreeNode(t1.val+t2.val)
            p.left=self.mergehelper(t1.left,t2.left)
            p.right=self.mergehelper(t1.right,t2.right)
        return p

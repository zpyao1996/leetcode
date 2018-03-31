class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not (root.left or root.right):
            if root.val==sum:
                return True
            else:
                return False
        else:
            sum=sum-root.val
            return self.hasPathSum(root.left,sum) or\
                   self.hasPathSum(root.right,sum)

a=TreeNode(1)
b=TreeNode(2)
a.right=b
asolution=Solution()
print(asolution.hasPathSum(a,3))
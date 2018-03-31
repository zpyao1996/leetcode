
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        Solution.mdepth=0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, 1)
        return Solution.mdepth

    @staticmethod
    def helper(node, i):
        if not(node.left or node.right):
            if i > Solution.mdepth:
                Solution.mdepth=i

        if node.left:
            Solution.helper(node.left,i+1)

        if node.right:
            Solution.helper(node.right, i + 1)


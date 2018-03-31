# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return ans
        queue=list()
        queue.append(root)
        while queue:
            ans.append(queue[-1].val)
            newqueue=list()
            for i in queue:
                if i.left:
                    newqueue.append(i.left)
                if i.right:
                    newqueue.append(i.right)
            queue=list(newqueue)
        return ans
a=TreeNode(1)
sol=Solution()
print(sol.rightSideView(a))

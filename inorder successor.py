
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        nodelist=list()
        nodelist.append(root)
        t=root
        while t.left:
            nodelist.append(t.left)
            t=t.left
        while nodelist:
            t=nodelist.pop()
            if t.right:
                nodelist.append(t.right)
                tp = t.right
                while tp.left:
                    nodelist.append(tp.left)
                    tp = t.left
            if t==p:
                return nodelist.pop() if nodelist else None

b=TreeNode(1)
c=TreeNode(2)
d=TreeNode(3)
b.left=c
b.right=d
a=Solution()
print(a.inorderSuccessor(b,b).val)
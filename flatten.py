# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
''' recursive solution
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flathelper(root)
        print(root)

    def flathelper(self,root):
        lflag=False
        rflag=False
        if not (root.left or root.right):
            return root,root
        if root.left:
            lflag=True
            lhead,ltail=self.flathelper(root.left)
            root.left=None
        if root.right:
            rflag=True
            rhead,rtail=self.flathelper(root.right)
        if not root.right:
            rtail=ltail
        if not lflag:
            root.right=rhead
        else:
            root.right = lhead
        if lflag and rflag:
            ltail.right=rhead
        return root,rtail
'''

# iterative solution
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack=list()
        stack.append(root)
        while len(stack):
            p=stack.pop()
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
            if not stack.len():
                p.right=stack[-1]
            p.left=None













a=TreeNode(1)
b=TreeNode(2)
#c=TreeNode(3)
a.left=b

sol=Solution()
sol.flatten(a)
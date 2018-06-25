# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.judgehelper(root)[0]

    def judgehelper(self,root):
        if root.left and root.right:
            a1, b1 = self.judgehelper(root.left)
            a2, b2 = self.judgehelper(root.right)
            return [a1 and a2 and abs(b1-b2)<=1,max(b1,b2)+1]
        elif root.left:
            _, b = self.judgehelper(root.left)
            return [b <= 1, b+1]
        elif root.right:
            _, b = self.judgehelper(root.right)
            return [b <=1 , b+1]
        else:
            return [True,1]
a=TreeNode(0)
b=TreeNode(1)
c=TreeNode(2)
d=TreeNode(3)
e=TreeNode(4)
f=TreeNode(5)
g=TreeNode(6)
a.left=b
a.right=c
b.left=d
b.right=e
d.left=f
d.right=g
sol=Solution()
print(sol.isBalanced(a))

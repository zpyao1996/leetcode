# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth=0
        lastlayer=0
        t = root

        while t:
            depth+=1
            t=t.left
        cur=root
        for i in range(depth-1):
            if self.isfull(cur.left,depth-1-i):
                cur=cur.right
                lastlayer=lastlayer*2+1
            else:
                cur=cur.left
                lastlayer=lastlayer*2
        if cur:
            lastlayer+=1
        return lastlayer+2**(depth-1)-1
    def isfull(self,root,curdepth):
        k=0
        while root:
            k+=1
            root=root.right
        return k==curdepth

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
#a.left=b
#a.right=c
sol=Solution()
print(sol.countNodes(a))
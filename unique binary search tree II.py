# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        ans=[[] for _ in range(n+1)]
        ans[0]=[0]
        ans[1]=[TreeNode(1)]
        for i in range(2,n+1):
            for j in range(1,i+1):
                for l in ans[j-1]:
                    for m in ans[i-j]:
                        if l==0: l=None
                        if m==0: m=None
                        root=TreeNode(j)
                        root.left=l
                        root.right=self.copytree(m,j)
                        ans[i].append(root)
        return ans[n]
    def copytree(self,root,n):
        if not root:
            return None
        newroot=TreeNode(root.val+n)
        if root.left:
            newroot.left=self.copytree(root.left,n)
        if root.right:
            newroot.right=self.copytree(root.right,n)
        return newroot
a=TreeNode(1)
b=TreeNode(2)
a.left=b
sol=Solution()
c=sol.generateTrees(3)
print(c)
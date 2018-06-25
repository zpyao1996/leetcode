# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        clist=[root]
        ans=[]
        while clist:
            newlist=[]
            ans.append([i.val for i in clist])
            for i in clist:
                if i.left:
                    newlist.append(i.left)
                if i.right:
                    newlist.append(i.right)
            clist=list(newlist)
        for i in range(len(ans)):
            if i^1==0:
                ans[i].reverse()
        return ans
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
a.left=b
a.right=c
sol=Solution()
print(sol.zigzagLevelOrder(a))
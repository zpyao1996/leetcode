# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        flag,number=self.findhelper(root,k)
        return number


    def findhelper(self,root,k):
        if not (root.left or root.right or k==1):
            return False,1
        stack = list()
        p = root
        while p:
            stack.append(p)
            p = p.left
        if k == 1:
            return True, stack.pop().val
        cursum=0
        while stack:
            anode = stack.pop()
            if k-cursum==1:
                return True,anode.val
            if anode.right:
                flag,number=self.findhelper(anode.right,k-1-cursum)
                if flag:
                    return flag, number
                else:
                    cursum += number+1
            else:
                cursum+=1
        return False,cursum

a=TreeNode(5)
b=TreeNode(1)
c=TreeNode(2)
d=TreeNode(3)
e=TreeNode(4)
a.left=b
b.right=c
c.right=d
d.right=e

sol=Solution()

print(sol.kthSmallest(a,5))

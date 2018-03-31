# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack1=list()
        visited=set()
        flag,a=self.findfirst(root,p,q,stack1,visited)
        if a==q:
            q=p
        stack2=list()
        self.findsecond(root,q,stack2,visited)
        for i in range(len(stack1)):
            if stack1[i]==stack2[i]:
                i+=1
            else:
                break
        return stack1[i-1]



    def findfirst(self,root,p,q,stack,visited):
        stack.append(root)
        if root==p or root==q:
            return True,root
        if root.left:
            flag,a=self.findfirst(root.left,p,q,stack,visited)
            if flag:
                return flag,a
        if root.right:
            flag,a=self.findfirst(root.right,p,q,stack,visited)
            if flag:
                return flag,a
        visited.add(root)
        stack.remove(root)
        return False,0

    def findsecond(self,root,q,stack,visited):
        stack.append(root)
        if root==q:
            return True
        if root.left and root.left not in visited:
            if self.findsecond(root.left,q,stack,visited):
                return True
        if root.right and root.right not in visited:
            if self.findsecond(root.right,q,stack,visited):
                return True
        visited.add(root)
        stack.remove(root)




a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
e=TreeNode(5)
d=TreeNode(4)
a.left=b
b.left=c
c.left=e
c.right=d
f=TreeNode(6)
b.right=f
sol=Solution()
print(sol.lowestCommonAncestor(a,d,f).val)


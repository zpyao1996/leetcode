# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
''' BFS solution
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        parentlist=[root]
        while parentlist:
            newlist=[]
            for i in parentlist:
                if i.left:
                    newlist.append(i.left)
                if i.right:
                    newlist.append(i.right)
            parentlist=list(newlist)
            for i in range(len(newlist)-1):
                newlist[i].next=newlist[i+1]
'''
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        first=root
        if not first:
            return
        while first.left:
            p=first
            while True:
                p.left.next=p.right
                if p.next:
                    p.right.next=p.next.left
                    p=p.next
                else:
                    break
            first=first.left

a=TreeLinkNode(1)
b=TreeLinkNode(2)
c=TreeLinkNode(3)
a.left=b
a.right=c
sol=Solution()
sol.connect(a)
print(a)
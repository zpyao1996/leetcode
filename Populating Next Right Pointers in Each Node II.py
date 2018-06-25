# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        first=root
        if not first:
            return
        while True:
            p=first
            first=None
            while p:
                if p.left:
                    first=p.left
                    break
                elif p.right:
                    first=p.right
                    break
                p=p.next
            if not first:
                break
            else:
                last = first
                if p.left and p.right:
                    p.left.next=p.right
                    last=p.right
                p=p.next
                while p:
                    if p.left:
                        last.next=p.left
                        last=last.next
                    if p.right:
                        last.next = p.right
                        last = last.next
                    p=p.next
a=TreeLinkNode(1)
b=TreeLinkNode(2)
c=TreeLinkNode(3)
a.left=b
a.right=c
sol=Solution()
sol.connect(a)
print(a)
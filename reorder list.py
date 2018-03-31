# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''use stack
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        stack=list()
        p=head
        while p:
            stack.append(p)
            p=p.next
        tail =stack.pop()
        p=head
        while True:
            pnext=p.next
            if p.next==tail:
                p.next=tail
                tail.next=None
                break
            elif p==tail:
                p.next=None
                break
            else:
                p.next=tail
                tail.next=pnext
            p=pnext
            tail=stack.pop()
    def printlist(self,a):
        while a:
            print(a.val)
            a=a.next
'''





a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
a.next=b
b.next=c
c.next=d
sol=Solution()
sol.reorderList(a)
sol.printlist(a)

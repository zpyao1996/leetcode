# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
''' not efficient
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummy=ListNode(0)
        dummy.next=head
        self.sorthelper(dummy,None)
        return dummy.next
    def sorthelper(self,head,end):
        if not (head.next and head.next.next):
            return
        if head.next==end or head.next.next==end:
            return
        dummy1=ListNode(0)
        dummy2=ListNode(0)
        dummy1.next=head.next
        dummy2.next=end
        t=head.next
        p=t.next
        while not p==end:
            pnext=p.next
            if p.val>=t.val:
                dummy2.next,p.next=p,dummy2.next
            else:
                dummy1.next,p.next=p,dummy1.next
            p=pnext
        head.next=dummy1.next
        t.next=dummy2.next
        self.sorthelper(head,t)
        self.sorthelper(t,end)

    def printlist(self, a):
        while a:
            print(a.val)
            a = a.next
'''

a=ListNode(5)
b=ListNode(2)
c=ListNode(8)
d=ListNode(4)
a.next=b
b.next=c
c.next=d
sol=Solution()
sol.printlist(sol.sortList(a))



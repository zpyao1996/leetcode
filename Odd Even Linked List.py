# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        odddummy=ListNode(0)
        odd=odddummy
        evendummy=ListNode(0)
        even=evendummy
        idx=1
        while p:
            if idx%2==1:
                odd.next=p
                odd=p
            else:
                even.next=p
                even=p
            p=p.next
            idx+=1
        odd.next=evendummy.next
        even.next=None
        return odddummy.next

sol=Solution()
a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c
def printlist(a):
    p=a
    while p:
        print(p.val)
        p=p.next
printlist(sol.oddEvenList(a))

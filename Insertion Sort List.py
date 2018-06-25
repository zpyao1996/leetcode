# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyhead=ListNode(0)
        while head:
            dummyhead,head=self.inserthelper(dummyhead,head)
        return dummyhead.next

    def inserthelper(self,dummyhead,p):
        pos=dummyhead
        while pos.next and pos.next.val<p.val:
            pos=pos.next
        pnext=p.next
        p.next=pos.next
        pos.next=p
        return dummyhead,pnext

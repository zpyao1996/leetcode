# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        last=None
        while p:
            p1=p
            p=p.next
            p1.next=last
            last=p1
        return last


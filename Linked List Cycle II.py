# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        fast,slow=dummy,dummy
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                break


        if not (fast.next and fast.next.next):
            return None
        else:
            fast=dummy
            while not fast==slow:
                fast = fast.next
                slow = slow.next
            return fast
a=ListNode(1)
b=ListNode(2)
a.next=b
b.next=a
sol=Solution()
print(sol.detectCycle(a).val)

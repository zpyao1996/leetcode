
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution(object):
    def swapPairs(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        while slow and slow.next:
            fast=slow.next
            a = slow.val
            slow.val = fast.val
            fast.val = a
            slow=slow.next.next
        return head




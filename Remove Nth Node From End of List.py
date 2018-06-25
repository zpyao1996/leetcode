# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy=ListNode(0)
        dummy.next=head
        liststack=[dummy]
        p = head
        while p:
            liststack.insert(0, p)
            p = p.next
        last = liststack[n]
        removed = liststack[n - 1]
        last.next = removed.next
        return dummy.next
a=ListNode(1)
sol=Solution()
print(sol.removeNthFromEnd(a,1))
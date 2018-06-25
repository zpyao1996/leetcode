# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        carry=0
        p=dummy
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            p.next=ListNode((val1+val2+carry)%10)
            if (val1+val2+carry)>=10:
                carry=1
            else:
                carry=0
            p=p.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy.next

a=ListNode(1)
b=ListNode(9)
c=ListNode(9)
b.next=c
sol=Solution()
def printlist(a):
    while a:
        print(a.val)
        a=a.next
printlist(sol.addTwoNumbers(a,b))
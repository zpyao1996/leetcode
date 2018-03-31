# Definition for singly-linked list with a random pointer.

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        s=RandomListNode(head.label)
        ans=s
        p=head
        visitset=set()
        visitset.add(head)
        wdict={}
        wdict[head]=s
        while p:
            if p.random:
                if p.random not in visitset:
                    visitset.add(p.random)
                    s.random=RandomListNode(p.random.label)
                    wdict[p.random]=s.random
                elif p.random==p:
                    s.random=s
                else:
                    s.random=wdict[p.random]
            if p.next:
                if p.next not in visitset:
                    visitset.add(p.next)
                    s.next=RandomListNode(p.next.label)
                    wdict[p.next]=s.next
                else:
                    s.next=wdict[p.next]
            p=p.next
            s=s.next
        return ans


'''
don't care about the internal structure until we copy all the nodes
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p=head
        dic={}
        while p:
            dic[p]=RandomListNode(p.label)
            p=p.next
        p=head
        while p:
            dic[p].random=dic[p.random]
            p=p.next
        return dic[head]
'''
sol=Solution()
a=RandomListNode(1)
a.random=a
sol.copyRandomList(a)



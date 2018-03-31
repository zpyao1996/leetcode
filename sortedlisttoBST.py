
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#bottom up solution
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        p=head
        length=0
        while p:
            length=length+1
            p=p.next
        return self.convert(head,0,length-1)

    def convert(self,head,start,end):
        if start>end:
            return None
        mid=(start+end)>>1
        left=self.convert(head,start,mid-1)
        root=TreeNode(head.val)
        head=head.next
        root.left=left
        root.right=self.convert(head,mid+1,end)
        return head


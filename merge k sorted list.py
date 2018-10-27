# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dum_head = ListNode(0)
        p = dum_head
        val_node_list = [[node.val, node] for node in lists if node]
        heapq.heapify(val_node_list)
        while val_node_list:
            _, c_node = heapq.heappop(val_node_list)
            p.next = c_node
            p = p.next
            if c_node.next:
                item = [c_node.next.val, c_node.next]
                heapq.heappush(val_node_list, item)
        return dum_head.next


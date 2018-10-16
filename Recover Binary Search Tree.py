# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result, node_list = [], []
        self.preorder_traverse(root, result, node_list)
        sorted_result = sorted(result)
        indices = [i for i in range(len(result)) if result[i]!=sorted_result[i]]
        idx1, idx2 = indices
        node_list[idx1].val, node_list[idx2].val =  node_list[idx2].val, node_list[idx1].val

    def preorder_traverse(self, node, result=[], node_list=[]):
        if node.left:
            self.preorder_traverse(node.left, result, node_list)
        result.append(node.val)
        node_list.append(node)
        if node.right:
            self.preorder_traverse(node.right, result, node_list)

a=TreeNode(3)
b=TreeNode(2)
c=TreeNode(4)
d=TreeNode(1)
a.left=b
b.left=d
b.right=c
sol=Solution()
sol.recoverTree(a)
result = []
sol.preorder_traverse(a, result)
print(result)
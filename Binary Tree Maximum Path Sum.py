# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_dict, right_dict, val_list = {}, {}, []
        self.get_max_helper(root, left_dict, right_dict, val_list)
        return max(val_list)

    def get_max_helper(self, root, left_dict, right_dict, val_list):
        if not root.left:
            left_max = 0
        else:
            left_max = self.get_max_helper(root.left, left_dict, right_dict, val_list)
        if not root.right:
            right_max = 0
        else:
            right_max = self.get_max_helper(root.right, left_dict, right_dict, val_list)
        half_max = max(root.val, left_max+root.val, right_max+root.val)
        left_dict[root] = left_max
        right_dict[root] = right_max
        val_list.append(max(0, left_max) + max(0, right_max) + root.val)
        return half_max

a=TreeNode(-10)
b=TreeNode(9)
a.left=b
sol=Solution()
print(sol.maxPathSum(a))

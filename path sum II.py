class Solution(object):
    def pathSum(self, root, sum):
        alist = list()
        listofl = list()
        self.pathhelper(root, sum, alist, listofl)
        return listofl

    def pathhelper(self, root, sum, alist, listofl):
        if not root:
            return
        sum = sum - root.val
        alist.append(root.val)
        if not (root.left or root.right):
            if sum == 0:
                listofl.append(list(alist))
        else:
            self.pathhelper(root.left, sum, alist, listofl)
            self.pathhelper(root.right, sum, alist, listofl)
        alist.pop()


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a=TreeNode(5)
b=TreeNode(4)
c=TreeNode(11)
d=TreeNode(2)
a.left=b
b.left=c
c.right=d
solution=Solution()
solution.pathSum(a,22)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    treemap=dict()
    ans=0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findhelper(root)
        return self.ans
    def findhelper(self,root):
        if not self.treemap.get(root,[]):
            if not (root.left or root.right):
                self.treemap[root]=True
                self.ans+=1
            else:
                if root.left:
                    self.findhelper(root.left)
                if root.right:
                    self.findhelper(root.right)
                lefttrue = True if not root.left or root.left and root.left.val == root.val and self.treemap[root.left] else False
                righttrue = True if not root.right or root.right and root.right.val == root.val and self.treemap[root.right] else False
                self.treemap[root]=lefttrue and righttrue
                if self.treemap[root]:
                    self.ans+=1

a="  7,82,82,-79,98,98,-79,-79,null,-28,-24,-28,-24,null,-79,null,97,65,-4,null,3,-4,65,3,null,97"
def stringToTreeNode(input):
    input = input.strip()
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

root=stringToTreeNode(a)
sol=Solution()
print(sol.countUnivalSubtrees(root))
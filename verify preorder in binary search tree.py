import math
class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        csmall=-math.inf
        nodestack=list()
        for i in preorder:
            if i<csmall:
                return False
            if not nodestack:
                nodestack.append(i)
            elif i<nodestack[-1]:
                nodestack.append(i)
            else:
                while nodestack and i>nodestack[-1]:
                    last=nodestack.pop()
                csmall=last
                nodestack.append(i)
        return True

Sol=Solution()
a=[10,3,1,6,2]
print(Sol.verifyPreorder(a))

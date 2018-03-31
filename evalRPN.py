import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numstack=list()
        while tokens:
            a=tokens.pop(0)
            if a=='+' or a=='-' or a=='/' or a=='*':
                e2=numstack.pop()
                e1=numstack.pop()
                if a=='+':
                    e1=e1+e2
                if a=='-':
                    e1=e1-e2
                if a=='*':
                    e1=e1*e2
                if a=='/':
                    e1=int(e1/e2)
                numstack.append(e1)
            else:
                numstack.append(int(a))
        return numstack.pop()

s=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol=Solution()
sol.evalRPN(s)
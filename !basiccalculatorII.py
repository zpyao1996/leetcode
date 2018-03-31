class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.replace(' ','')
        if not s:
            return 0
        operands=list()
        operators=list()
        start=end=0
        alloperators=['+','-','*','/']
        while end<len(s):
            if s[start] in alloperators:
                operators.append(s[start])
                start=end=start+1
            else:
                while end<len(s) and s[end] not in alloperators:
                    end+=1
                anum=int(s[start:end])
                operands.append(anum)
                if operators:
                    aoperator=operators[-1]
                    if aoperator=='*':
                        b=operands.pop()
                        a=operands.pop()
                        operands.append(a*b)
                    if aoperator=='/':
                        b = operands.pop()
                        a = operands.pop()
                        operands.append(int(a / b))
                start=end
        while operators:
            aoperator=operators.pop(0)
            if aoperator == '+':
                a = operands.pop(0)
                b = operands.pop(0)
                operands.insert(0,a + b)
            if aoperator == '-':
                a = operands.pop(0)
                b = operands.pop(0)
                operands.insert(0,a-b)
        return operands[0]

test= "0-2147483647"
sol=Solution()
print(sol.calculate(test))
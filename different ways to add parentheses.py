import re
import operator

class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        tokens = re.split('(\+|-|\*)', input)
        length = (len(tokens) + 1) // 2
        if length == 0:
            return []

        for i in range(0, len(tokens), 2):
            tokens[i] = int(tokens[i])
        if length == 1:
            return [tokens[0]]
        ans = [[[] for _ in range (length)] for _ in range(length)]
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        return self.findhelper(tokens,ops,0,length-1,ans)

    def findhelper(self,tokens,ops,start,end,ans):
        if not ans[start][end]==[]:
            return ans[start][end]
        if start==end:
            ans[start][end]=[tokens[2*start]]
            return ans[start][end]
        elif start==end-1:
            ans[start][end] = [ops.get(tokens[2 * start + 1])(tokens[2 * start ], tokens[2 * start+2])]
            return ans[start][end]
        else:
            for j in range(start,end):
                ans[start][end]+=[ops.get(tokens[2*j+1])(l,m) for l in self.findhelper(tokens,ops,start,j,ans) for m in self.findhelper(tokens,ops,j+1,end,ans)]
            return ans[start][end]

sol=Solution()
print(sol.diffWaysToCompute("2*3-4*5"))



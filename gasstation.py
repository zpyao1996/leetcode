class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        if length==1:
            if(gas[0]>=cost[0]):
                return 0
            else:
                return -1
        residual=[]
        for i in range(length):
            residual=residual+[gas[i]-cost[i]]
        start=0
        end=1
        rest=gas[0]-cost[0]
        while not start==end:
            if rest<0:
                start=(start-1+length)%length
                rest=rest+residual[start]
            else:
                end=(end+1+length)%length
                rest=rest+residual[end-1]
        if rest<0:
            return -1
        else:
            return start
gas=[1,2]
cost=[2,1]
sol=Solution()
print(sol.canCompleteCircuit(gas,cost))
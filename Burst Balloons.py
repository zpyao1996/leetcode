

class Solution(object):
    def calgain(self,state,pos,nums):
        left,right=pos-1,pos+1
        while left>-1 and state[left]==1:
            left-=1
        left=1 if left==-1 else nums[left]
        while right<len(state) and state[right]==1:
            right +=1
        right=1 if right==len(state) else nums[right]
        return left*nums[pos]*right
    def flip(self,oristates,scores,nums):
        states=[]
        for state in oristates:
            positions=[i for i in range(len(state)) if state[i]==0]
            for i in positions:
                oriscore=scores[self.list2str(state)]
                newstate=list(state)
                newstate[i]=1
                if self.list2str(newstate) not in scores:
                    scores[self.list2str(newstate)]=self.calgain(state,i,nums)+oriscore
                else:
                    scores[self.list2str(newstate)]=max( scores[self.list2str(newstate)],self.calgain(state, i, nums) + oriscore)
                states.append(newstate)
        return states
    def list2str(self,numlist):
        return(''.join(map(str, (numlist))))
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        states=[[0]*len(nums)]
        scores={self.list2str(states[0]):0}
        for i in range(len(nums)):
            states=self.flip(states,scores,nums)
        return scores[self.list2str(states[0])]
sol=Solution()
print(sol.maxCoins([3,1,5,8]))
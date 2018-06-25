class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        clist=[]
        ans=[]
        self.permutehelper(nums,ans,clist)
        return ans
    def permutehelper(self,nums,ans,clist):
        if not nums:
            ans.append(list(clist))
            return
        else:
            for i in range(len(nums)):
                a=nums.pop(i)
                clist.append(a)
                self.permutehelper(nums,ans,clist)
                clist.remove(a)
                nums.insert(i,a)
sol=Solution()
print(sol.permute([1,2,3]))

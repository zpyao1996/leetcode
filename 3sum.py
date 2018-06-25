class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            partans= self.twosum(nums[i+1:],-nums[i])
            if partans:
                for j in partans:
                    if not [nums[i]]+j in ans:
                        ans.append([nums[i]]+j)
        return (ans)
    def twosum(self,nums,target):
        ans=[]
        numdict={}
        for i in nums:
            if i in numdict:
                ans.append([i,numdict[i]])
            else:
                numdict[target-i]=i
        return ans
sol=Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))


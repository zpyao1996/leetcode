class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        sum1=[0 for _ in range(len(nums))]
        sum2=[0 for _ in range(len(nums))]
        sum1[0]=0
        sum2[0]=nums[0]
        for i in range(1,len(nums)):
            sum1[i]=max(sum1[i-1],sum2[i-1])
            sum2[i]=max(sum1[i-1]+nums[i],sum2[i-1])
        return max(sum1[-1],sum2[-1])
sol=Solution()
print(sol.rob([1,3,4]))
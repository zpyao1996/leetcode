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
        sum1[0]=nums[0]
        sum1[1]=nums[0]
        sum2[0]=0
        sum2[1]=nums[1]
        for i in range(2,len(nums)):
            if not i==len(nums)-1:
                sum1[i] =max(sum1[i-2]+nums[i],sum1[i-1])
                sum2[i] = max(sum2[i - 2] + nums[i], sum2[i - 1])
            else:
                sum1[i]=sum1[i-1]
                sum2[i] = max(sum2[i - 2] + nums[i], sum2[i - 1])
        return max(sum1[-1],sum2[-1])
sol=Solution()
sol.rob([0,0,0])
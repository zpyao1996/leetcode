class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        normal=1
        reversed=1
        ans=[1]*len(nums)
        for i in range(len(nums)):
            ans[i]=ans[i]*normal
            normal=normal*nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*reversed
            reversed=reversed*nums[i]
        return ans
sol=Solution()
print(sol.productExceptSelf([]))


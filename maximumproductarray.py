class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cmax=nummax=nummin=nums[0]
        for i in range(1,len(nums)):
            a=[nummax*nums[i],nummin*nums[i],nums[i]]
            nummax=max(a)
            nummin=min(a)
            cmax=max(cmax,nummax)
        return cmax


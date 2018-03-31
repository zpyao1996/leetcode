class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start=0
        end=len(nums)-1
        while True:
            if start==end:
                return nums[start]
            mid = int((start + end) / 2)
            if nums[mid]>=nums[start] and nums[mid]>nums[end]:
                start=mid+1
            elif nums[mid]<nums[end] and nums[mid]<=nums[start]:
                end=mid
            else:
                return nums[start]

a=[1,2,3,4,5]
sol=Solution()
print(sol.findMin(a))


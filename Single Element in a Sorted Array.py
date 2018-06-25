class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)//2
        while start<=end:
            if start==end:
                return nums[2*start]
            mid = (start + end) // 2
            if nums[2*mid]==nums[2*mid+1]:
                start=mid+1
            else:
                end=mid
a=[1,2,2]
sol=Solution()
print(sol.singleNonDuplicate(a))


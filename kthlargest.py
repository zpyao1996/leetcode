class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        return self.findhelper(nums,k)

    def findhelper(self,nums,k):
        pos= self.partition(nums)
        length=len(nums)
        if pos==length-k:
            return nums[pos]
        if pos<length-k:
            return self.findhelper(nums[pos+1:],k)
        else:
            return self.findhelper(nums[:pos],k+pos-length)

    def partition(self, nums):
        low = l=0
        r=len(nums)-1
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low

sol=Solution()
print(sol.findKthLargest([2,1],1))
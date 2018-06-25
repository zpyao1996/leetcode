class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        median=self.findmedian(nums)

    def partition(self,nums):
        l=low=0
        r=len(nums)-1
        pivot=nums[r]
        while l<r:
            if nums[l]<pivot:
                nums[l],nums[low]=nums[low],nums[l]
                low+=1
            l+=1
        nums[r],nums[low]=nums[low],nums[r]
        return low
    def findmedian(self,nums):
        index=len(nums)//2
        return self.findkthsmallest(nums,index)
    def findkthsmallest(self,nums,index):
        low=self.partition(nums)
        if low==index:
            return nums[index]
        elif low<index:
            return self.findkthsmallest(nums[low+1:],index-low-1)
        else:
            return self.findkthsmallest(nums[:low],index)

'''
easier　way
class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
'''
sol=Solution()
print(sol.findmedian([1,5,34,6,7,9,5]))

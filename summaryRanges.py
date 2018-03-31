class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ans=[]
        start=end=0
        while end<len(nums):
            while end+1<len(nums) and nums[end+1]==nums[end]+1:
                end=end+1
            if end==start:
                ans.append(str(nums[start]))
            else:
                ans.append(str(nums[start])+'->'+str(nums[end]))

            start = end + 1
            end = end + 1
        return ans



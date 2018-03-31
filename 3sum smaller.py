class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans=0
        for k in range(len(nums)):
            i=0
            j=k-1
            while i<j:
                if nums[i] + nums[j] + nums[k] < target:
                    ans+=j-i
                    i+=1
                else:
                    j-=1
        return ans


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        left=0
        right=1
        numset=set([nums[0]])
        while right<len(nums):
            if right==left+k+1:
                numset.remove(nums[left])
                left+=1
            if nums[right] in numset:
                return True
            numset.add(nums[right])
            right+=1
        return False


a=[1]
sol=Solution()
print(sol.containsNearbyDuplicate(a,0))

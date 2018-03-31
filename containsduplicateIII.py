
''' too slow, TLE
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(len(nums)-1):
            for j in range(i+1,min(i+k,len(nums)-1)+1):
                if abs(nums[i]-nums[j])<=t:
                    return True
        return False
'''
#bucket sort
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k:
                del d[nums[i - k] / w]
        return False


nums=[1,2,4,1]
k=4
t=1
sol=Solution()
print(sol.containsNearbyAlmostDuplicate(nums,k,t))

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _len = len(nums)
        nums += [-1, -1]
        for i, v in enumerate(nums[:-1]):
            if 1 <= v <= _len and i != v:
                nums[v], nums[i] = nums[i], nums[v]
                while 1 <= nums[i] <= _len and nums[i] != nums[nums[i]]:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        for i in range(1, _len + 2):
            if i != nums[i]: return i

a = [11,4,10,1,2,6]
sol=Solution()
sol.firstMissingPositive(a)
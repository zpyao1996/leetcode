class Solution:
    def findDuplicate(self, nums):
        i = nums[0]
        while i != nums[i]:
            nums[i], i = i, nums[i]
        return i
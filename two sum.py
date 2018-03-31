class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buff_dict = {}
        if len(nums) <= 1:
            return []
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict(nums[i]), i]
            else:
                buff_dict[target-nums[i]]=i



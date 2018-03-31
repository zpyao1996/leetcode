class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = end = 0
        flag = False
        cmin = len(nums)
        sum = nums[0]
        while end < len(nums):
            if sum >= s:
                flag = True
                length = end + 1 - start
                cmin = min(cmin, length)
                sum -= nums[start]
                start = start + 1
            else:
                end = end + 1
                if end < len(nums):
                    sum += nums[end]
        if flag:
            return cmin
        else:
            return 0


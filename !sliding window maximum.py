from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        c_queue = sorted([[num, idx] for idx, num in enumerate(nums[:k])],
                         reverse=True)
        c_queue = deque(c_queue)
        print(c_queue)
        if k > len(nums):
            return ans


nums = [1,3,-1,-3,5,3,6,7]
k = 3
sol=Solution()
print(sol.maxSlidingWindow(nums, k))
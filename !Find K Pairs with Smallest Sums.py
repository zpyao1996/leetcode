import heapq

# speed up hint: maintain the heap with length no larger than k
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        nums1 = nums1[:k]
        nums2 = nums2[:k]
        sumheap = list()
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(sumheap, (num1 + num2, [num1, num2]))
        ans_list = []
        for _ in range(min(k, len(sumheap))):
            smallsum = heapq.heappop(sumheap)
            ans_list.append(smallsum[1])
        return ans_list
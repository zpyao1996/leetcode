class Solution(object):
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                            l // 2)) / 2.0

    def findKth(self, A, B, k):
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            return self.findKth(A[i:], B[:j], j)


    # Brute Force
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        m = len(nums)
        if m % 2 == 0:
            return (nums[m // 2 - 1] + nums[m // 2]) / 2
        else:
            return nums[m // 2]


sol = Solution()
array1 = []
array2 = [2,3,4,5,6]
array1 = [1,2]
array2 = [1,1]

print(sol.findMedianSortedArrays(array1, array2))
print(sol.findMedianSortedArrays1(array1, array2))
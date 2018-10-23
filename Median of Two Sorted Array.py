from bisect import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        is_odd = (len1 + len2) % 2 == 1
        return_idx = (len1 + len2) // 2
        def binary_search(nums1, nums2, return_idx):
            len1, len2 = len(nums1), len(nums2)
            if len1 < len2:
                nums1, nums2 = nums2, nums1
                len1, len2 = len2, len1
            mid2 = len2 // 2
            num2 = nums2[mid2]
            insert_idx = bisect(nums1, num2)
            if mid2 + insert_idx == return_idx:
                if is_odd:
                    return max(num2, nums1[insert_idx])
                else:
                    return (num2 + nums1[insert_idx]) / 2
            elif mid2 + insert_idx < return_idx:
                nums1 = nums1[insert_idx:]
                return_idx -= insert_idx - 1
            else:
                nums1 = nums1[:insert_idx]
            return binary_search(nums1, nums2, return_idx)
        return binary_search(nums1, nums2, return_idx)


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
array1 = [1,2,3,4,5]
array2 = [2,3,4,5,6]
# array1 = [1,3]
# array2 = [2]
array1 = [1]
array2 = [1]
print(sol.findMedianSortedArrays(array1, array2))
print(sol.findMedianSortedArrays1(array1, array2))
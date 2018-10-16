class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        cmax = min(height[left], height[right]) * (right - left)
        while True:
            if height[left] < height[right]:
                cheight = height[left]
                while left < right and height[left] <= cheight:
                    left += 1
            else:
                cheight = height[right]
                while left < right and height[right] <= cheight:
                    right -= 1
            carea = min(height[left], height[right]) * (right - left)
            cmax = max(cmax, carea)
            if left == right:
                return cmax

A = [1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(A))
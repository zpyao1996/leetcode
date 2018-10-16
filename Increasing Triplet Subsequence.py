class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        c_num = nums[0]
        c_pair = None
        for num in nums[1:]:
            if c_pair and num > c_pair[1]:
                return True
            elif c_pair and num < c_pair[1]:
                if num > c_pair[0]:
                    c_pair[1] = num
                    c_pair[0] = c_num
                elif num < c_pair[0]:
                    if c_num < num:
                        c_pair = [c_num, num]

            elif not c_pair and num > c_num:
                c_pair = [c_num, num]
            c_num = min(c_num, num)
        return False
sol = Solution()
a = [2,1,5,0,3]
print(sol.increasingTriplet(a))

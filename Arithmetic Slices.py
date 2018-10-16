class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if (not A) or len(A)<2:
            return 0
        ans = 0
        diff_list = [A[i+1] - A[i] for i in range(len(A) - 1)]
        # keep the record of current state
        cstate = [diff_list[0], 1]
        for diff in diff_list[1:]:
            if diff == cstate[0]:
                cstate[1] += 1
                ans += max(0, cstate[1] - 1)
            else:
                cstate = [diff, 1]
        return ans

A = [1, 2, 3, 8, 9, 10]
sol = Solution()
print(sol.numberOfArithmeticSlices(A))


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if (not A) or (len(A)<3):
            return 0
        ans = 0
        diff_list = [[None], [[A[1] - A[0], 1]]]
        for idx in range(2, len(A)):
            cur_diff_list = [[A[idx] - A[0], 1]]
            for pre_idx in range(1, idx):
                cur_diff = A[idx] - A[pre_idx]
                count = sum([count for [diff, count] in
                             diff_list[pre_idx] if diff == cur_diff])
                cur_diff_list.append([cur_diff, count + 1])
                ans += count
            diff_list.append(cur_diff_list)
        return ans

A=[2,4,6,8,10,12]
sol=Solution()
print(sol.numberOfArithmeticSlices(A))
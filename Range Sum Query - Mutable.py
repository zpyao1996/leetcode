import numpy as np


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        length = len(nums)
        self.nums = nums
        self.num_division = int(np.sqrt(length))
        self.sub_sum_list = []
        self.division_idx = []
        for i in range(self.num_division):
            start = int(length * i / self.num_division)
            end = int(length * (i + 1) / self.num_division)
            self.sub_sum_list.append(sum(nums[start:end]))
            self.division_idx.append(start)

    def get_interval_idx(self, idx):
        for i, division_idx in enumerate(self.division_idx):
            if division_idx > idx:
                return i - 1
        return self.num_division - 1

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        old_num = self.nums[i]
        self.nums[i] = val
        interval_idx = self.get_interval_idx(i)
        self.sub_sum_list[interval_idx] += val - old_num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        interval_idx_i = self.get_interval_idx(i)
        interval_idx_j = self.get_interval_idx(j)
        if interval_idx_i == interval_idx_j:
            return sum(self.nums[i: j+1])
        else:
            ans = 0
            ans += sum(self.nums[i: self.division_idx[interval_idx_i + 1]])
            ans += sum(self.nums[self.division_idx[interval_idx_j]: j + 1])
            ans += sum(self.sub_sum_list[interval_idx_i + 1 : interval_idx_j])
            return ans

# Your NumArray object will be instantiated and called as such:
nums = [-28,-39,53,65,11,-56,-65,-39,-43,97]
obj = NumArray(nums)
print(obj.sumRange(5,6))
obj.update(9,27)
print(obj.sumRange(2,3))
print(obj.sumRange(6,7))
obj.update(1,-82)
obj.update(3,-72)
print(obj.sumRange(3,7))
print(obj.sumRange(1,8))
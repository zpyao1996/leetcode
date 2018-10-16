from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = list(set(nums))
        start_pts_dict, end_pts_dict = {}, {}
        mid_pts_dict = defaultdict(list)
        parent_list = [i for i in range(len(nums))]
        for idx, num in enumerate(nums):
            if num in start_pts_dict:
                pre_idx = start_pts_dict.pop(num)
                parent_list[pre_idx] = idx
                if num - 1 in end_pts_dict:
                    end = end_pts_dict.pop(num - 1)
                    mid_pts_dict[num - 1] = [end, idx]
                else:
                    start_pts_dict[num - 1] = idx
            elif num in end_pts_dict:
                pre_idx = end_pts_dict.pop(num)
                parent_list[idx] = pre_idx
                if num + 1 in start_pts_dict:
                    start = start_pts_dict.pop(num + 1)
                    mid_pts_dict[num + 1] = [idx, start]
                else:
                    end_pts_dict[num + 1] = idx
            elif num in mid_pts_dict:
                left, right = mid_pts_dict.pop(num)
                parent_list[idx] = left
                parent_list[right] = idx
            else:
                if num - 1 in end_pts_dict:
                    end = end_pts_dict.pop(num - 1)
                    mid_pts_dict[num - 1] = [end, idx]
                else:
                    start_pts_dict[num - 1] = idx
                if num + 1 in start_pts_dict:
                    start = start_pts_dict.pop(num + 1)
                    mid_pts_dict[num + 1] = [idx, start]
                else:
                    end_pts_dict[num + 1] = idx
        return self.count(parent_list)

    def count(self, parent_list):
        weight_dict = defaultdict(int)
        for idx, num in enumerate(parent_list):
            def getparent(parent_list, idx):
                while parent_list[idx] != idx:
                    idx = parent_list[idx]
                return idx
            weight_dict[getparent(parent_list, idx)] += 1
        return max(weight_dict.values())


sol=Solution()
a = [-1,-9,-5,-2,-9,8,-8,1,-9,-3,-3]
print(sol.longestConsecutive(a))





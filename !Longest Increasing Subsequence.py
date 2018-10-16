from collections import defaultdict
class Solution(object):
    # so stupid solution
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # list of tuples, (length, list)
        ans_dict = defaultdict(list)
        ans_dict[1] = [nums[0]]
        for num in nums[1:]:
            new_dict = ans_dict.copy()
            for count in ans_dict:
                num_list = ans_dict[count]
                pos = len(num_list)
                while num <= num_list[pos-1] and pos >= 1:
                    pos -= 1
                length = pos + 1
                if length in new_dict.keys():
                    clist = num_list[:pos] + [num]
                    orilist = new_dict[length]
                    def listcompare(clist, orilist):
                        assert len(clist) == len(orilist)
                        pos = len(clist) - 1
                        while pos >=0 :
                            if clist[pos] > orilist[pos]:
                                return False
                            elif clist[pos] < orilist[pos]:
                                return True
                            else:
                                pos -= 1
                        return True
                    new_dict[length] = clist if listcompare(clist, orilist) else orilist
                else:
                    new_dict[length] = num_list[:pos] + [num]
            ans_dict = new_dict
        return sorted(list(ans_dict.keys()))[-1]

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        anslist = [1]
        for idx in range(1, len(nums)):
            cmax = 1
            for pre_idx in range(0, idx):
                if nums[idx] > nums[pre_idx]:
                    cmax = max(cmax, anslist[pre_idx] + 1)
            anslist.append(cmax)
        return max(anslist)




sol = Solution()
a = [3,5,6,2,5,4,19,5,6,7,12]
print(sol.lengthOfLIS(a))


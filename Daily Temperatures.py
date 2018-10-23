from bisect import bisect
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        temp_list, idx_list = [], []
        ans_list = []
        for idx, temperature in enumerate(T[::-1]):
            insert_idx = bisect(temp_list, temperature)
            if insert_idx == len(temp_list):
                ans_list.append(0)
                temp_list.append(temperature)
                idx_list.append(idx)
            else:
                closest_idx = idx_list[insert_idx]
                ans_list.append(idx - closest_idx)
                temp_list.insert(insert_idx, temperature)
                idx_list.insert(insert_idx, idx)
            def filter_list(temp_list, idx_list,
                            temperature, idx, insert_idx):
                for temp, idx in zip(temp_list[:insert_idx],
                                     idx_list[:insert_idx]):
                    if temp <= temperature:
                        temp_list.remove(temp)
                        idx_list.remove(idx)

            filter_list(temp_list, idx_list, temperature, idx, insert_idx)
        return ans_list[::-1]

T = [73, 74, 75, 71, 69, 72, 76, 73]
sol = Solution()
print(sol.dailyTemperatures(T))

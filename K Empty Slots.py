import bisect
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        def binary_search(cur_flowers, pos):
            length = len(cur_flowers)
            start, end = 0, length
            idx = length // 2
            while True:
                if cur_flowers[idx] > pos:
                    end = idx
                else:
                    start = idx + 1
                if start == end:
                    return start
                idx = (start + end) // 2
        if not flowers:
            return -1
        cur_flowers = [flowers[0]]
        for day, pos in enumerate(flowers[1:]):
            insert_idx = binary_search(cur_flowers, pos)
            cur_flowers.insert(insert_idx, pos)
            if insert_idx != 0 and pos - cur_flowers[insert_idx - 1] == k + 1 \
        or insert_idx != len(cur_flowers)-1 and cur_flowers[insert_idx + 1] - pos == k + 1:
                return day + 2
        return -1

    def kBloomingSlots(self, flowers, k):
        start_pos, end_pos, intervals, state_list = \
            [flowers[0]], [flowers[0]], [1], [k == 1]
        for pos in flowers[1:]:
            insert_idx = bisect.bisect(start_pos, pos)
            if (insert_idx != 0 and pos == end_pos[insert_idx - 1] + 1) and \
        (insert_idx != len(start_pos) and pos == start_pos[insert_idx] - 1):
                start_pos.pop(insert_idx)
                end_pos.pop(insert_idx - 1)
                intervals[insert_idx - 1] += 1 + intervals[insert_idx]
                intervals.pop(insert_idx)
            elif insert_idx != 0 and pos == end_pos[insert_idx - 1] + 1:
                end_pos[insert_idx - 1] = pos
                intervals[insert_idx - 1] += 1
            elif (insert_idx != len(start_pos) and pos == start_pos[insert_idx] - 1):
                start_pos[insert_idx] = pos
                intervals[insert_idx] += 1
            else:
                start_pos.insert(insert_idx, pos)
                end_pos.insert(insert_idx, pos)
                intervals.insert(insert_idx, 1)
            state_list.append(k in intervals)
        days = [idx + 1 for idx, state in enumerate(state_list) if state]
        if not days:
            return -1
        else:
            return max(days)


sol=Solution()
print(sol.kBloomingSlots([1,4,7,5,6,2,3],3))
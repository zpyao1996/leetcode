from itertools import product, permutations
import numpy as np
class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        digits = sorted({int(i) for i in time if i != ':'}, reverse=True)
        if len(digits) == 1:
            return time
        cur = [int(i) for i in time if i != ':']
        temp, ans = list(cur), None
        def is_valid(digits):
            return digits[0]*10+digits[1]<24 and digits[2]*10+digits[3]<60
        for pos in range(len(cur) - 1, -1, -1):
            for digit in digits:
                temp[pos] = digit
                if not is_valid(temp):
                    continue
                if temp > cur:
                    ans = list(temp)
                elif ans:
                    break
            if ans:
                break
        if not ans:
            ans = temp
        return '{}{}:{}{}'.format(*ans)

    # cannot duplicate digits
    def nextClosestTime2(self, time):
        # brute force
        """
        :type time: str
        :rtype: str
        """
        cur = tuple(int(i) for i in time if i != ':')
        all_candidate = permutations(cur, 4)
        valid_candidate = [i for i in all_candidate if i[0] * 10 +
                           i[1] < 24 and i[2] * 10 + i[3] < 60]
        def convert_to_time(digits):
            return 10*digits[0]+digits[1], 10*digits[2]+digits[3]
        def get_time_diff(cur, next_t):
            cur_h, cur_min = convert_to_time(cur)
            next_h, next_min = convert_to_time(next_t)
            if next_h < cur_h or next_h == cur_h and next_min <= cur_min:
                next_h += 24
            if next_min < cur_min:
                next_min += 60
                next_h -= 1
            return next_min - cur_min + (next_h - cur_h) * 60
        time_diffs = [get_time_diff(cur, next_t) for next_t in valid_candidate]
        idx = np.argmin(time_diffs)
        return '{}{}:{}{}'.format(*valid_candidate[idx])

    def nextClosestTime1(self, time):
        # brute force
        """
        :type time: str
        :rtype: str
        """
        cur = tuple(int(i) for i in time if i != ':')
        digit_set = set(cur)
        all_candidate = product(digit_set, repeat = 4)
        valid_candidate = [i for i in all_candidate if i[0] * 10 +
                           i[1] < 24 and i[2] * 10 + i[3] < 60]
        def convert_to_time(digits):
            return 10*digits[0]+digits[1], 10*digits[2]+digits[3]
        def get_time_diff(cur, next_t):
            cur_h, cur_min = convert_to_time(cur)
            next_h, next_min = convert_to_time(next_t)
            if next_h < cur_h or next_h == cur_h and next_min <= cur_min:
                next_h += 24
            if next_min < cur_min:
                next_min += 60
                next_h -= 1
            return next_min - cur_min + (next_h - cur_h) * 60
        time_diffs = [get_time_diff(cur, next_t) for next_t in valid_candidate]
        idx = np.argmin(time_diffs)
        return '{}{}:{}{}'.format(*valid_candidate[idx])

sol = Solution()

print(sol.nextClosestTime2('23:59'))
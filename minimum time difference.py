class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def time_converter(time_str):
            hour, minute = time_str.split(':')
            return int(hour) * 60 + int(minute)
        length = len(timePoints)
        converted_list = sorted(set(map(time_converter, timePoints)))
        if len(converted_list) < length:
            return 0
        converted_list.append(converted_list[0] + 1440)
        c_min = 1440
        for i in range(len(converted_list) - 1):
            c_min = min(c_min, converted_list[i + 1] - converted_list[i])
        return c_min

sol = Solution()
time1 = '23:59'
time2 = '00:00'
print(sol.findMinDifference([time1, time2]))
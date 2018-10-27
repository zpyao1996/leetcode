import random
from bisect import bisect


class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.sum_list = []
        c_sum = 0
        for weight in w:
            c_sum += weight
            self.sum_list.append(c_sum)
        self.total_weight = self.sum_list[-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        seed = random.randint(0, self.total_weight - 1)
        return bisect(self.sum_list, seed)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
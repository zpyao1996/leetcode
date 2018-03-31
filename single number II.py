class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict={}
        for i in nums:
            numdict[i]=numdict.get(i,0)+1
        for j in numdict:
            if numdict[j]==1:
                return j

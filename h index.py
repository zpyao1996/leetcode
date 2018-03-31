class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        length=len(citations)
        i=1
        while i <= length and citations[length-i]>=i:
            i+=1
        return i-1
sol=Solution()
print(sol.hIndex([1]))



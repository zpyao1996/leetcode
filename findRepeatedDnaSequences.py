class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strset=set()
        ans=set()
        for i in range(len(s)-9):
            astr=s[i:i+10]
            if astr in strset:
                ans.add(astr)
            else:
                strset.add(astr)
        return list(ans)



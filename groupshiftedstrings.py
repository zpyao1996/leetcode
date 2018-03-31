class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        stringdict=dict()
        for i in strings:
            flag=False
            for j in stringdict:
                if self.validshift(i,j):
                    stringdict.get(j).append(i)
                    flag=True
            if not flag:
                stringdict[i]=[i]
        return list(stringdict.values())

    def validshift(self,a,b):
        if not len(a)==len(b):
            return False
        else:
            diff=(ord(b[0])-ord(a[0])+26)%26
            for i in range(len(a)):
                if not (ord(b[i])-ord(a[i])+26) % 26==diff:
                    return False
            return True

a=['a','b','ab','za']
sol=Solution()

print(sol.groupStrings(a))
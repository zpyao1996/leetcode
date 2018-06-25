class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        chardict = {}
        reversedict={}
        ans=0
        for i in t:
            if i in chardict.keys():
                ans=ans^chardict[i]
            else:
                chardict[i]=len(chardict)
                ans=ans^chardict[i]
                reversedict[chardict[i]]=i
        for j in s:
            ans=ans^chardict[j]
        return reversedict[ans]

sol=Solution()
print(sol.findTheDifference('ae','aea'))
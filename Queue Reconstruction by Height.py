
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        heightdict=dict()
        for i in people:
            if i[0] in heightdict:
                heightdict[i[0]].append(i[1])
            else:
                heightdict[i[0]] = [i[1]]
        keys=sorted(list(heightdict.keys()),reverse=True)
        ans=[]
        for i in keys:
            heightdict[i].sort()
            for j in heightdict[i]:
                ans.insert(j,[i,j])
        return ans

'''
a more concise method, dict is not necessary
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people==[]:
            return []
        people.sort(key=lambda x:(x[0],-x[1]),reverse=True)
        res=[]
        for i in people:
            res.insert(i[1],i)

        return res
'''

a=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sol=Solution()
sol.reconstructQueue(a)
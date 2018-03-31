# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b


class Solution(object):
    nets=[[0,1],[1,2],[2,3]]
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack = [0]
        numlist=list(range(1,n))
        while stack:
            cur = stack.pop()
            flag = False
            for i in numlist:
                if knows(cur, i):
                    stack.append(i)
                    numlist.remove(i)
                    break
        for i in range(n):
            if i != cur and (not knows(i, cur) or knows(cur,i)) :
                return -1
        return cur

def knows(a,b):
    return True if [a,b] in sol.nets else False

sol=Solution()
print(sol.findCelebrity(4))



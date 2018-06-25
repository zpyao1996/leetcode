


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class Points:
    def __init__(self, n,a=0, b=0):
        self.x = a
        self.y = b
        self.n=n
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points)<2:
            return len(points)
        points.sort(key=lambda z:z.x)
        left=0
        right=1
        newpoints=[]
        while right<len(points):
            while right<len(points) and points[left].x== \
                    points[right].x and points[left].y==points[right].y:
                right+=1
            newpoints.append(Points(right-left,points[left].x,points[left].y))
            left = right
        points=newpoints
        ans=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x:
                    slope='inf'
                else:
                    slope=(points[j].y-points[i].y)/float(points[j].x-points[i].x)
                ans.append((points[i],slope,points[i].n,points[j].n))
        if len(points)==1:
            return points[0].n
        ansdict={}
        for i in ans:
            if i[:2] in ansdict:
                ansdict[i[:2]]+=i[3]
            else:
                ansdict[i[:2]]=i[2]+i[3]
        return max(ansdict.values())

a=Point(0,0)
b=Point(94911151,94911150)
c=Point(94911152,94911151)
d=[a,b,c]
d.sort(key=lambda z:z.x)

sol=Solution()
print(sol.maxPoints([a,b,c]))

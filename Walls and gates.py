class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return None
        ylen=len(rooms[0])
        xlen=len(rooms)
        queue = [[x, y] for x in range(xlen)
                     for y in range(ylen) if rooms[x][y] == 0]
        dist = 1
        while queue:
            newqueue=[]
            for x,y in queue:
                if x-1>=0 and rooms[x-1][y]==2147483647:
                    rooms[x-1][y]=dist
                    newqueue.append([x-1,y])
                if x+1<xlen and rooms[x+1][y] == 2147483647:
                    rooms[x+1][y] = dist
                    newqueue.append([x+1, y])
                if y-1>=0 and rooms[x][y-1] == 2147483647:
                    rooms[x][y-1] = dist
                    newqueue.append([x, y-1])
                if y+1<ylen and rooms[x][y+1] == 2147483647:
                    rooms[x][y+1] = dist
                    newqueue.append([x, y+1])
            queue=list(newqueue)
            dist=dist+1

a=[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
b=Solution()
b.wallsAndGates(a)
print(a)

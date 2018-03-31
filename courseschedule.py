class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph=[[] for _ in range(numCourses)]
        for x,y in prerequisites:
            graph[x].append(y)
        visit=[0 for _ in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(i,graph,visit):
                return False
        return True

    def dfs(self,i,graph,visit):
        visit[i]=-1
        astack=list()
        astack.append(i)
        while astack:
            a=astack.pop()
            for j in graph[a]:
                if visit[j]==-1:
                    return True
                elif visit[j]==0:
                    visit[j]=-1
                    astack.append(j)
                else:
                    continue
            visit[a]=0

        return False

sol=Solution()
print(sol.canFinish(3,[[1,2],[0,1],[0,2]]))



class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n==1 and not edges:return True
        if len(edges)!=n-1:
            return False
        adjacent={i:[] for i in range(n)}
        for i,j in edges:
            adjacent[i].append(j)
            adjacent[j].append(i)
        visited=set()
        visited.add(edges[0][0])
        nodequeue=[edges[0][0]]
        while nodequeue:
            a=nodequeue.pop(0)
            for j in adjacent[a]:
                if j in visited:
                    return False
                else:
                    visited.add(j)
                    adjacent[j].remove(a)
                    nodequeue.append(j)
        return True

edges = [[1,0],[1,2],[2,3]]
sol=Solution()
print(sol.validTree(4,edges))



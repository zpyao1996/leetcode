import numpy as np
class Solution(object):
    # Wrong algorithm: think about it
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def floyd(dist, n):
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]
            return dist
        dist = np.ones([n, n]) * n
        for start, end in edges:
            dist[start][end] = 1
            dist[end][start] = 1
        for i in range(n):
            dist[i][i] = 0
        dist = floyd(dist, n)
        height = np.max(dist, axis = 0)
        idx = np.where(height == min(height))
        return list(idx[0])


    def _findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # find all leave nodes
        def is_leave_node(idx, edges):
            count = sum([idx in edge for edge in edges])
            return count == 1
        def get_father(leave_node, edges, visited):
            father_list = []
            for edge in edges:
                if leave_node in edge:
                    if edge[0] == leave_node:
                        if edge[1] not in visited:
                            father_list.append(edge[1])
                    else:
                        if edge[0] not in visited:
                            father_list.append(edge[0])
            return father_list
        visited = set()
        c_layer_set = set()
        for i in range(n):
            if is_leave_node(i, edges):
                c_layer_set.add(i)
                visited.add(i)
        while True:
            new_layer_set = set()
            for node in c_layer_set:
                father_list = get_father(node, edges, visited)
                for father_node in father_list:
                    new_layer_set.add(father_node)
                    visited.add(father_node)
            if not new_layer_set:
                return list(c_layer_set)
            c_layer_set = new_layer_set

sol=Solution()
n = 7

edges = [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]]
print(sol.findMinHeightTrees(n, edges))

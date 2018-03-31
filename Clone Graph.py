# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        visit={}
        s=UndirectedGraphNode(node.label)
        stack=[node]
        visit[node.label]=s
        while stack:
            p=stack.pop()
            for j in p.neighbors:
                if j.label not in visit:
                    visit[j.label]=UndirectedGraphNode(j.label)
                    stack.append(j)
                visit[p.label].neighbors.append(visit[j.label])
        return s









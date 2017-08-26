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
            return
        d = {}
        self.aux(node, d)
        return d[node]

    def aux(self, node, d):
        if node in d:
            return d[node]
        t = UndirectedGraphNode(node.label)
        d[node] = t
        for neighbor in node.neighbors:
            t.neighbors.append(self.aux(neighbor, d))
        return t

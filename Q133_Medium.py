# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        q = [node]
        mapping = {}
        while q:
            n = q.pop(0)
            copynode = self.copy(mapping, n)
            if copynode.neighbors ==[]:
                for i in n.neighbors:
                    copyn = self.copy(mapping, i)
                    copynode.neighbors.append(copyn)
                    q.append(i)
        return mapping[node]
#         if  node==None:
#             return None
#         queue,mapping=[node],{}
        
#         while queue:
#             entry=queue.pop(0)
#             copyentry=self.copy(mapping, entry)
#             if copyentry.neighbors==[]:
#                 for link in entry.neighbors:
#                     copylink=self.copy(mapping,link)
#                     copyentry.neighbors.append(copylink)
#                     queue.append(link)
#         return mapping[node] 
        
    
    def copy(self, mapping, node):
        if node not in mapping:
            mapping[node] = UndirectedGraphNode(node.label)
        return mapping[node]
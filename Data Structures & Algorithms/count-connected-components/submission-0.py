class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjmap = {}
        visited = n * [False] 
        for i in range(n): 
            adjmap[i] = []
        for node1,node2 in edges:
            adjmap[node1].append(node2)
            adjmap[node2].append(node1)
        
        def dfs(node): 
            
            for neighbor in adjmap[node]: 
                if not visited[neighbor]: 
                    visited[neighbor] = True
                    dfs(neighbor)
        res = 0
        for node in range(n):
            if not visited[node]: 
                visited[node] = True
                dfs(node)
                res += 1
        
        return res
            
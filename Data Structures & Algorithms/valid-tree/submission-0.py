class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # we need to first initialize a an adjacency list this is
        # so that we dont get any false positives 

        nodeMap = {}

        for i in range(n): 
            nodeMap[i] = []
        for node1, node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)
        
        visited = set()
        
        def dfs(curr_node,prev_node): 
            if curr_node in visited:
                return False
            
            visited.add(curr_node)
            
            for neighbors in nodeMap[curr_node]: 
                if neighbors == prev_node: 
                    continue
                if not dfs(neighbors,curr_node):
                    return False 
            
            return True
        
        return dfs(0,-1) and n == len(visited)
            
                

        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        '''
            Problem Approach/Notes: 
                create an adjecency list in order to track the nodes/edges 
                going to initialzie a visited list initialzied to False * len(edges) + 1 
                
                Basically we are just going to iterate over the edges, call a dfs
                and see if there has been an edge that has been visited before
                if so return the edge pair otherwise return []

        '''
        num_of_nodes = len(edges) + 1 
        adjmap = {}
        for n in range(num_of_nodes): 
            adjmap[n] = []
        
        def dfs(curr_node, parent_node): 
            #if current node is visited that means you have detected a cycle
            if visited[curr_node] == True: 
                return True
            #else mark it as True and continue the dfs 
            visited[curr_node] = True
            
            for nei in adjmap[curr_node]: 
                if nei == parent_node: 
                    continue #getting rid of false positives
                if dfs(nei,curr_node):
                    return True 
            return False

        
        for u,v in edges: 
            adjmap[u].append(v)
            adjmap[v].append(u)
            visited = [False] * num_of_nodes
            
            if dfs(u,-1): 
                return  [u,v]
        return []
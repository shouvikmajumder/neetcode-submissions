class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
            Problem Approach/Notes:
                Topological Sort

                A course has 3 possible states: 
                    visited --> crs has been added to ouput 
                    visiting --> crs not added to output, but added to cycle 
                    unvisited --> crs not added to ouput or cycle
            
            Key note: 
                A node is being put in a cycle during the processing of the course, 
                once a cycle is detected you immediately stop the program 

                If a node is fully processed, you can then add it to visiteds meaning 
                that it is a valid course 
        '''

        preMap = {}
        visited , cycle = set(), set()        
        output = []
        for i in range(numCourses): 
            preMap[i] = []
        for course, pre in prerequisites: 
            preMap[course].append(pre)

        def dfs(course): 
            if course in cycle: 
                return False 
            if course in visited: 
                return True

            cycle.add(course)

            for pre in preMap[course]:
                if not dfs(pre): 
                    return False 
            cycle.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for course in preMap: 
            if not dfs(course): 
                return []
        
        return output


        

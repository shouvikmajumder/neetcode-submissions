class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        '''
            The genral idea is that we are going to do a dfs on every course, which is going to have connected prereqs to it
            and if it can run the entire dfs without failign then you would return True

            Get a preqrequesist map of number of courses, each course should be initailized to an 
            empty list. 

            We can then iterate throught the prerequisites list where the course is going to be the key 
            and the value is going to be the prereq that is going to be appended to the list of prerequisites

            In order to determine if it is not possible to finish all courses, we need to determine 
            if there is a cycle in the graph, therefore we would need to initialzie a visited set
            
            base cases in dfs: if we have seen the course of if the premap of the cours is empty: return True

            if None of the base cases have been triggered, we are visiting a new course, in which case we need to 
            add it to the visited set

            We can then run a dfs of every prereq that course requires and if it doesnt return anything 
            we can remove it from visited 
            and we can set the prereq vlaue in the mapping to [] and once it recurses back 
            itll return as true 

        '''
        preMap = {}
        visited = set()
        for i in range(numCourses): 
            preMap[i] = []
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        
        def dfs(course):
            # if the pereqmap is empty you can take that course 
            if preMap[course] == []:
                return True 
            # if the course you have taken is already in the visited set you cant take the course 
            if course in visited:
                return False
            # else you have seen a couse that you haven't seen before
            visited.add(course)
            # need to loop throught and check if prereqs are valid
            for pre in preMap[course]:
                if not dfs(pre):
                    return False 
            # if you can run throught every pre without a cycle 
            visited.remove(course)
            preMap[course] = []
            
            return True

        for course in preMap:
            if not dfs(course): 
                return False 
        return True 










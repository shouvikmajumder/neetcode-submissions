class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        visited = {}

        for word in strs: 
            key = "".join(sorted(word))

            if key not in visited:
                visited[key] = []
            visited[key].append(word)
        
        return (list(visited.values()))
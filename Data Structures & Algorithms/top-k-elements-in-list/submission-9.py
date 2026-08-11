class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        visited = {}

        for number in nums: 
            if number not in visited:
                visited[number] = 0 
            visited[number] += 1 
        
        vals = sorted(visited.values())[::-1][:k]

        output = []

        for key in visited:
            if visited[key] in vals: 
                output.append(key)
        return output
            
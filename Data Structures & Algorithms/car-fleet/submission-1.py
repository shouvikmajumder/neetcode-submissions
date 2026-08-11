class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out = 0
        hashmap = {}

        for i in range(len(position)):
            hashmap[position[i]] = (target- position[i])/speed[i]
            
        hashlst = list(hashmap.keys())
        hashlst = sorted(hashmap)
        
        index = 0
        while(index<len(hashlst)-1):
            j = index + 1
            if hashmap[hashlst[index]]>=hashmap[hashlst[j]]:
                out += 1
            index += 1
            
                
        return out


            
        


    



class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
    #position will be the key time will be the value
        for i in range(len(position)):
            hashmap[position[i]] = (target - position[i])/(speed[i])
        print(hashmap)
        
        stack = [] 
        
        hashmaplst = sorted(list(hashmap.keys()))
        
        for i in range(len(hashmaplst)):
            if i == 0: 
                stack.append(hashmaplst[i])
            else: 
                if hashmap[hashmaplst[i]]<hashmap[hashmaplst[i-1]]:
                    stack.append(hashmaplst[i])
        return len(stack)

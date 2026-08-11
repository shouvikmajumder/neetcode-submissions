class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):

            curr = i + 1

            while(curr<len(temperatures)):
                if temperatures[curr] > temperatures[i]:
                    res[i] = curr - i
                    break
                curr += 1
                
        return res

            
            


            
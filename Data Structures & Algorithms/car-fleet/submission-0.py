class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        out = []

        for i in range(len(position)):
            val = (target - position[i])/speed[i]
            if val not in out:
                out.append(val)
        
        return int(len(out))



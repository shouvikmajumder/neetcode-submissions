class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out += i + ","
        return out

    def decode(self, s: str) -> List[str]:
        out= []
        outstr = ""
        for i in s: 
            if i == ",":
                out.append(outstr)
                outstr = ""
            else: 
                outstr += i
                
        return out
        

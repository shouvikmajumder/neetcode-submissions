class Solution:

    def encode(self, strs: List[str]) -> str:
        outstr = ""
        for i in strs:
            outstr += i + "/"
        return outstr


    def decode(self, s: str) -> List[str]:

        outlst = []
        outstr ="" 

        for i in s: 
            if i == "/":
                outlst.append(outstr)
                outstr = ""
            else:
                outstr += i 
        return outlst



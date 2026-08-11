class Solution:

    def encode(self, strs: List[str]) -> str:
        outstr = ""
        for i in strs:
            outstr += i + "+"
        return outstr


    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else :
            return s[:-1].split("+")


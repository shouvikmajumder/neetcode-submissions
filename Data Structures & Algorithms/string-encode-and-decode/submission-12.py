class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = ""
        for word in strs: 
            print(word)
            res += word  + "_"
        return res[:-1]

    def decode(self, s: str) -> List[str]:
        output_lst = s.split("_")
        return output_lst
        
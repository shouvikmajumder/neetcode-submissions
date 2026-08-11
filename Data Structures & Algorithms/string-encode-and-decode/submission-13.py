class Solution:

    def encode(self, strs: List[str]) -> str: 
        res = ""
        for word in strs:
            res += word + "/n"

        print(res)
        return res



    def decode(self, s: str) -> List[str]:
        output_lst = s.split("/n")        
        return output_lst[:-1]
        
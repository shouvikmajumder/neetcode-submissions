class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in strs:
            encoded_str += i + "/n"  

        return encoded_str
    
    def decode(self, s: str) -> List[str]:

        output_lst = s.split("/n")

        return output_lst[:-1]
        
        
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for i in strs:
            encoded_str += i + " "  

        return encoded_str
    
    def decode(self, s: str) -> List[str]:

        output_lst = s.split()
        return output_lst
        
        
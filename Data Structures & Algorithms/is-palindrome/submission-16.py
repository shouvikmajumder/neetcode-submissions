class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        parse_lst = []

        for i in s:
            if i.isalpha() or i.isdigit():
                parse_lst.append(i.lower())
        
        
        l,r = 0, len(parse_lst) - 1

        while(l<r):
            if parse_lst[l] != parse_lst[r]:
                return False
            l +=1
            r -=1 
        return True
        
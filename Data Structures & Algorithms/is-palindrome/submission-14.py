class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = []

        for i in s:
            if i.isalpha() and i.isdigit() == False: 
                lst.append(i)
        
        l,r = 0, len(lst)-1 
        
        while (l<r):
            if lst[l].lower() != lst[r].lower():
                return False
            l +=1
            r-=1
        return True


    

            

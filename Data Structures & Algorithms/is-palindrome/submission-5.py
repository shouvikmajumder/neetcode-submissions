class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []

        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
        
        x = 0
        y= len(newlist)-1
        while(x<=len(newlist)-1):
            if(newlist[x]!=newlist[y]):
                return False
            x+=1
            y-=1
        return True
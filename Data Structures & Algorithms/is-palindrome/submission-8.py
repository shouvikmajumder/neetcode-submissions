class Solution:
    def isPalindrome(self, s: str) -> bool:
        newlist = []
        # if len(s) <=2:
        #     return False
        for i in s:
            if i.isalpha():
                newlist.append(i.lower())
            elif isinstance(i,int):
                newlist.append(i)
        
        x = 0
        y= len(newlist)-1
        while(x<=len(newlist)-1):
            if(newlist[x]!=newlist[y]):
                return False
            x+=1
            y-=1
        return True
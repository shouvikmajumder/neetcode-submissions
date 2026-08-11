class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
    
        check_perm_s1 = {}
        check_perm_s2 = {}
        
        for index in range(len(s1)):
            if s1[index] not in check_perm_s1:     
                check_perm_s1[s1[index]] = 0
            if s2[index] not in check_perm_s2:
                check_perm_s2[s2[index]] = 0
            check_perm_s1[s1[index]] += 1
            check_perm_s2[s2[index]] += 1
        
        print(check_perm_s1)
        print(check_perm_s2)

        left, right = 0, len(s1)-1 
        
        while right <= len(s2) -1 : 
            if check_perm_s1 == check_perm_s2: 
                return True

            print(check_perm_s1,check_perm_s2)
            
            if right + 1 < len(s2):
                next_char = s2[right + 1]  

                if next_char not in check_perm_s2: 
                    check_perm_s2[next_char] = 1
                elif next_char in check_perm_s2: 
                    check_perm_s2[next_char] += 1

            char = s2[left]
            check_perm_s2[char] -= 1     
            if check_perm_s2[s2[left]] == 0: 
                del check_perm_s2[s2[left]]
         
            left += 1 
            right += 1
            
            

        return False
        

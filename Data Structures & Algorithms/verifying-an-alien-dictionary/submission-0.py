class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        alien_orderings = {}
        
        for index in range(len(order)): 
            character = order[index]
            alien_orderings[character] = index
        
        if len(words) == 1:
            return True

        for index in range(1,len(words)):
            
            word1, word2 = words[index -1], words[index]

            for j in range(len(word1)):
                if j > len(word2) -1: 
                    return False 
                
                if alien_orderings[word1[j]] > alien_orderings[word2[j]]:
                    return False
                elif alien_orderings[word1[j]] < alien_orderings[word2[j]]:
                    break

        return True
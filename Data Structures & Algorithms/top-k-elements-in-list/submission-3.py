class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap= {}
        topk= []

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            elif i in hashmap:
                hashmap[i] +=1
                # Hashmap is complete
        #sorting algo here
        # curr = None 
        
        
        hashlst = list(hashmap.keys())

        if (len(hashlst) == 1):
            return hashlst


        for index in range(len(hashlst[1:])):
            prev = index -1

            currkey = (hashlst[index]) #keys theselves
            prevkey = (hashlst[prev])

            currval = hashmap[currkey]
            prevval = hashmap[prevkey]
            
            if topk == []:
                topk.append(prevkey)
            if currval>= prevval:
                topk.insert(0,currkey)
            elif currval<= prevval:
                topk.append(currkey)

        return topk[:k]
        
            
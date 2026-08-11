class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        outputlist = []
        for s in strs:
            reorder = ( "".join(sorted(s)))
            if reorder not in hashmap:
                hashmap[reorder] = []
            hashmap[reorder].append(s)
        return list(hashmap.values())
            
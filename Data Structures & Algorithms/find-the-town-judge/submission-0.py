class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_lst = {}
        
        for i in range(1,n + 1): 
            adj_lst[i] = []
        for trustor, trustee in trust: 
            adj_lst[trustor].append(trustee)

        # find the key with no truste
        judge = None
        for key in adj_lst: 
            if adj_lst[key] == []:
                judge = key
                break 

        if not judge: 
            return -1

        for key in adj_lst:
            if key == judge:
                continue
            if judge not in adj_lst[key]:
                return -1 
        
        return judge

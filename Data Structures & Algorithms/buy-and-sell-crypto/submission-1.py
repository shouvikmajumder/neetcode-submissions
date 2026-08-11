class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        proflst= [0]
        l,r = 0,1

        while(r<= len(prices)-1):
            if prices[l] < prices[r]:
                proflst.append(prices[r]- prices[l])
            else: 
                l = r
            r += 1 
        return max(proflst)
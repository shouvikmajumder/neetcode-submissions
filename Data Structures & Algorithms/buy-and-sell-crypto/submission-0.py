class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices)[::-1]:
            return 0
        
        newlist = []
        
        for i in range(len(prices[:-1])):
            for j in range(i,len(prices)):
                newlist.append(prices[j]-prices[i])
        return max(newlist)
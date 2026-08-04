class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        best=0
        for i in range(len(prices)-1):
            for r in range(l,len(prices)):
                best=max(best,prices[r]-prices[l])
            
            l+=1
            r=l
        
        return best




        
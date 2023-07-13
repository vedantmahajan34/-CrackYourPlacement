class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j=0,1
        n=len(prices)
        profit = 0
        while j<n:  
            if prices[j-1] > prices[j]:
                profit+= prices[j-1] -prices[i]
                prices[i]= prices[j]
            j+=1
        return max(profit,profit + prices[n-1]-prices[i])
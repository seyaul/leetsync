class Solution:
    def maxProfit(self, prices):
        maxProf = 0
        l, r = 0, 1
        while r < len(prices):
            if maxProf < prices[r] - prices[l]:
                maxProf = prices[r] - prices[l]
                r+=1
            elif prices[r] - prices[l] < 0:
                l+=1
                r=l+1
            else: 
                r+=1
        return maxProf

    
        
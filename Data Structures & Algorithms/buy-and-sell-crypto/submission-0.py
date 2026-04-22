class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_sofar=prices[0]
        profit=0
        for i in prices:
            if i< min_sofar:
                min_sofar=i
            else:
                profit=max(profit,i-min_sofar)
        return profit

        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far=prices[0]
        profit=0
        for i in range(0,len(prices)):
            if prices[i]<min_so_far:
                min_so_far=prices[i]
            else:
                profit=max(profit,prices[i]-min_so_far)
        return profit

        
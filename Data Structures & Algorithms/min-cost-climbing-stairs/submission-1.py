class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==1:
            return cost[0]
        if len(cost)==2:
            return min(cost[0],cost[1])
        
        p1=cost[0]
        p2=cost[1]
        i=2
        while i< len(cost):
            curr = min(p1,p2) + cost[i]
           
            p1=p2
            p2=curr
            i+=1
        return min(p1,p2)          


        
        
        
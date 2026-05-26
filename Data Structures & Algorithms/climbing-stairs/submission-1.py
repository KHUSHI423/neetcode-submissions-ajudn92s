class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        #space optimization
        if n<=2:
            return n
        prev=0
        curr=1
        while n:
            prev,curr=curr,curr+prev
            n-=1
        return curr
        '''
        
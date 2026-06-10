class Solution:
    def hammingWeight(self, n: int) -> int:
        res =0
        while n!=0:
            n &=(n-1)
            res+=1
        return res
        '''        
        count=0
        for i in range(32):
            if n&1==1:
                count+=1
            n>>=1
        return count
        '''
        
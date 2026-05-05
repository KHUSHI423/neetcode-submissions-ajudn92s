class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_len=0x7fffffff
        mask=0xffffffff
        while b!=0:
            carry = (a & b)<<1
            a=( a^b)&mask
            b=carry
        return a if a < max_len else ~(a & mask)
        
        
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xorr=n
        for i in range(n):
            xorr^=i^ nums[i]
        return xorr
        '''
        nums.sort()
        for i in range(len(nums)):
            if i ^ nums[i] !=0:
                return i
        return len(nums)
        '''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=[0]*n
        suffix=[0]*n
        prev=1
        for i in range(n):
            prefix[i]=prev
            prev*=nums[i]
        nx=1
        for i in range(n-1,-1,-1):
            suffix[i]=nx
            nx*=nums[i]
        for i in range(n):
            nums[i]=prefix[i]*suffix[i]
        return nums
        
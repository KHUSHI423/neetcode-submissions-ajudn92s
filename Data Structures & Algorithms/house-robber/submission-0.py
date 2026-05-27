class Solution:
    def rob(self, nums: List[int]) -> int:
        #space optimization
        p1=nums[0]
        p2=0
        i=1
        while i < len(nums):
            ans = max(p2 + nums[i] , p1 )
            p2=p1
            p1=ans
            i+=1
        return max(p1,p2)


        
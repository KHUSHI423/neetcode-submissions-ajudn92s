class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = [0] * len(nums)
        p[0] = nums[0]
        for i in range(1,len(nums)):
            curr = p[i-1] * nums[i]
            if curr < p[i-1]:
                p[i] = 1
            else:
                p[i] = curr
        return max(p)
        
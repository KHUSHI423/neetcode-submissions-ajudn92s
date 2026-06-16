class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = float('-inf')
        prefix = 1
        suffix =  1
        for i in range(len(nums)):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[len(nums) -1 - i]
            maximum = max(maximum,max(prefix,suffix))
        return maximum
        
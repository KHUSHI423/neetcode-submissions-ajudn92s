class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        index=0
        for i in range(len(nums)):
            index=index^nums[i]
        return index
        
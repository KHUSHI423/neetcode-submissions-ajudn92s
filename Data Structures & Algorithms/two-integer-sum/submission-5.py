class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            s=abs(target-nums[i])
            if s in freq:
                return [freq[s],i]
            freq[nums[i]]=i
        return []
           
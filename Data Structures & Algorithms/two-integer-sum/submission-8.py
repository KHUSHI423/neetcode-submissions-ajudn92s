class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            n=target-nums[i]
            if n in freq:
                return [freq[n],i]
            else:
                freq[nums[i]]=i+freq.get(nums[i],0)
        return None
        
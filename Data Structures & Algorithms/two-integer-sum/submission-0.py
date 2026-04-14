class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            s=target-nums[i]
            if s in hash_map:
                return [hash_map[s],i]
            hash_map[nums[i]]=i
        return []
        
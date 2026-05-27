class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            prev2 = 0
            prev1 = 0

            for num in arr:
                curr = max(prev1, num + prev2)
                prev2 = prev1
                prev1 = curr

            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            solve(nums[:-1]),
            solve(nums[1:])
        )


        
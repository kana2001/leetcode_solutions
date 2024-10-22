class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        target = n

        for i in range(n-1, -1, -1):
            if nums[i] + i >= target:
                target = i
        return target == 0
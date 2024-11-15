class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l,r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[l] + nums[r]
                if curr > target:
                    r -= 1
                elif curr < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


        # -4, -1. -1, 0. 1, 2

        # -1, -1, 2
        # -1, 0, 2
        
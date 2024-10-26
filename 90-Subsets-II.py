class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = []
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(stack[:])
                return

            stack.append(nums[i])
            
            dfs(i+1)
            stack.pop()
            notInclude = nums[i]
            while i + 1 < len(nums) and nums[i+1] == notInclude:
                i += 1
            dfs(i+1)
        dfs(0)
        return res

            
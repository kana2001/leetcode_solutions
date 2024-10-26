class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        stack = []
        def dfs():
            if len(stack) == n:
                res.append(stack[:])
                return
            
            for i in range(n):
                if not used[i]:
                    stack.append(nums[i])
                    used[i] = True
                    dfs()
                    used[i] = False
                    stack.pop()
        dfs()
        return res

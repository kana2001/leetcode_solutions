class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []

        def dfs(i, curr):
            if i >= len(candidates) or curr > target:
                return
            if curr == target:
                res.append(stack[:])
                return
            
            stack.append(candidates[i])
            dfs(i, curr + candidates[i])
            stack.pop()
            dfs(i + 1, curr)
        dfs(0, 0)
        return res

        
        
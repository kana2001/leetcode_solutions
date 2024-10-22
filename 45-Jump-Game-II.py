class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])

        visited = set()
        while q:
            idx, jumps = q.popleft()
            if idx == len(nums) - 1:
                return jumps
            for i in range(1, nums[idx] + 1):
                newIdx = i + idx
                if newIdx not in visited and newIdx < len(nums):
                    visited.add(newIdx)
                    q.append((newIdx, jumps+1))
                
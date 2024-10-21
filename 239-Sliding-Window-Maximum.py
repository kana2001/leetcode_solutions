class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        for i in range(k):
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], k + i))

        res = [q[0][0]]
        for i in range(k, len(nums)):
            if q[0][1] == i:
                q.popleft()
            while q and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], k + i))
            res.append(q[0][0])
        return res



        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for n in numSet:
            length = 0
            if n-1 not in numSet:
                while n + length in numSet:
                    length += 1
                res = max(length, res)
        return res
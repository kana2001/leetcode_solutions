class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            if len(minHeap) == k:
                if n > minHeap[0]:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap, n)
            else:
                heapq.heappush(minHeap, n)
        return minHeap[0]

        
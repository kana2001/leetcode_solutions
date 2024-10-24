class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        minHeap = []
        for n in freq:
            if len(minHeap) == k and freq[n] > minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (freq[n], n))
            elif len(minHeap) < k:
                heapq.heappush(minHeap, (freq[n], n))
        
        return [minHeap[i][1] for i in range(len(minHeap))]
        
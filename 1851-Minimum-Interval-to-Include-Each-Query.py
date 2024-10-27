class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        minHeap = []
        intervals.sort()
        res = [0] * len(queries)

        queries_ordered = []
        for i in range(len(queries)):
            queries_ordered.append((queries[i], i))
        queries_ordered.sort()

        i = 0
        for (q, _) in (queries_ordered):
            while i < len(intervals) and intervals[i][0] <= q:
                if q <= intervals[i][1]:
                    heapq.heappush(minHeap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i+=1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[_] = minHeap[0][0] if minHeap else -1
        return res
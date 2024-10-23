class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((w, v))
        heapq.heappush(minHeap, (0, k)) # it takes 0 time for the source to recieve
        received = set()
        while minHeap:
            currTime, node = heapq.heappop(minHeap)
            if node in received:
                continue

            received.add(node)
            if len(received) == n:
                return currTime
            
            for nei in adj[node]:
                dt, dst = nei
                heapq.heappush(minHeap, (currTime + dt, dst))
        return -1

        
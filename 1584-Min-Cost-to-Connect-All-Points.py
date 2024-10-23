class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visit = set()
        minHeap = []
        adj = defaultdict(list)
        for i, p in enumerate(points):
            x,y = p
            for j in range(len(points)):
                if i == j:
                    continue
                nx, ny = points[j]
                man_dist = abs(x - nx) + abs(y - ny)
                adj[i].append((man_dist, j))

        heapq.heappush(minHeap, (0,0))
        res = 0
        while len(visit) != len(points):
            cost, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for nei in adj[node]:
                heapq.heappush(minHeap, nei)
        return res

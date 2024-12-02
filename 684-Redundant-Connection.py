class UF:
    def __init__(self, size):
        self.par = [i for i in range(size)]
        self.rank = [1] * size 
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] > self.rank[root_y]:
            self.par[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.par[root_x] = root_y
        else:
            self.par[root_y] = root_x
            self.rank[root_x] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UF(len(edges) + 1) 
        for x,y in edges:
            if not uf.union(x,y):
                return [x,y]

        
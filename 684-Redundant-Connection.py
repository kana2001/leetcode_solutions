class UF:
    def __init__(self, size):
        self.par = [i for i in range(size)]
    def find(self, x):
        res = x
        if res != self.par[x]:
            res = self.find(self.par[x])
        return res
    def union(self, x, y):
        if self.find(x) == self.find(y):
            return False
        self.par[self.find(x)] = self.par[self.find(y)]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for x,y in edges:
            nodes.add(x)
            nodes.add(y)
        uf = UF(len(nodes) + 1)

        res = []
        for x,y in edges:
            if not uf.union(x,y):
                res = [x,y]
        return res

        
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        adj = defaultdict(list)
        for idx, c in enumerate(s):
            l = r = idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                adj[l].append(s[l:r+1])
                l -= 1
                r += 1
            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                adj[l].append(s[l:r+1])
                l -= 1
                r += 1
        part = []
        res = []
        def dfs(idx):
            if idx < 0 or idx > len(s):
                return
            if idx == len(s):
                res.append(part[:])
                return
            for pal in adj[idx]:
                part.append(pal)
                dfs(idx + len(pal))
                part.pop()
        dfs(0)
        return res
            



        
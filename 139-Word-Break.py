class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True
        wordSet = set(wordDict)
        for i in range(n-1, -1, -1):
            for j in range(i, n+1):
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
        return dp[0]
                
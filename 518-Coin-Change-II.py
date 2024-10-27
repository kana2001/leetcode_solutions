class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * len(coins) for i in range(amount+1)]
        for i in range(len(coins)):
            dp[0][i] = 1

        for a in range(1,amount + 1):
            for i in range(len(coins) -1, -1, -1):
                include_coin = dp[a-coins[i]][i] if a-coins[i] >= 0 else 0
                exclude_coin = dp[a][i+1] if i+1 < len(coins) else 0
                dp[a][i] = include_coin + exclude_coin
        return dp[amount][0]
        
        
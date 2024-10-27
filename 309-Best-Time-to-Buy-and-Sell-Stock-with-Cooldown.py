class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # must buy before sell
        # cant buy 2 at a time
        # sell, must increment day by 2

        # buy, sell, or cooldown
        dp = {}
        def dfs(haveStock, day):
            if day >= len(prices):
                return 0
            if (haveStock, day) in dp:
                return dp[((haveStock, day))]
            res = 0
            if haveStock:
                # sell or cool down
                sell = dfs(False, day + 2) + prices[day]
                cooldown = dfs(True, day + 1)
                res += max(sell, cooldown)
            else:
                buy = dfs(True, day + 1) - prices[day]
                cooldown = dfs(False, day + 1)
                res += max(buy, cooldown)
            dp[(haveStock, day)] = res
            return res
        return dfs(False, 0)
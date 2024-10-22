class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            return 1 if s != '0' else 0

        n = len(s)
        dp1,dp2 = 0,0
        dp2 = 1 if s[n-1] != '0' else 0
        if s[n-2] != '0':
            dp1 = dp2
            if s[n-2] == '2' and s[n-1] in '0123456':
                dp1 += 1
            elif s[n-2] == '1':
                dp1 += 1

        for i in range(n - 3, -1, -1):
            curr = 0
            if s[i] != '0':
                curr += dp1
            if s[i] == '2' and s[i+1] in '0123456':
                curr += dp2
            elif s[i] == '1':
                curr += dp2
            dp1, dp2 = curr, dp1
        return dp1



        
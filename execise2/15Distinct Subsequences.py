def numDistinct(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ori = len(s)
        tar = len(t)
        dp = [[0 for _ in range(ori+1)] for _ in range(tar+1)]
        for i in range(ori+1):
                dp[0][i] = 1
        for i in range(tar):
                for j in range(ori):
                        tt = t[i]
                        o = s[j]
                        if o==tt:
                                dp[i+1][j+1] = dp[i][j]+dp[i+1][j]
                        else:
                                dp[i+1][j+1] = dp[i+1][j]
        # print(dp)
        return dp[-1][-1]
def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        buy = 0
        if not prices:
                return 0
        buy = prices[0]
        pre = 0
        for p in prices:
                if p < pre:
                        if pre > buy:
                                res+=pre-buy
                                buy = p
                                pre = p
                                continue
                        if p<buy:
                                buy = p
                pre = p
        if pre > buy:
                res+=pre-buy
        return res
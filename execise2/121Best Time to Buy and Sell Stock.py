def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
                return 0
        minP = prices[0]
        res = 0
        for x in prices:
                if x < minP:
                        minP = x
                        continue
                t = x - minP
                if t>res:
                        res = t
        return res
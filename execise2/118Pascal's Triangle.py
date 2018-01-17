def generate(numRows):
        """
        :type numRows: int
        :rtype: List
        """
        if numRows==1:
                return [[1]]
        if numRows ==2:
                return [[1],[1,1]]
        res = [[1],[1,1]]
        for row in range(3,numRows+1):
                r = [1]
                pre = res[-1]
                for i in range(1,row-1):
                        p = pre[i]+pre[i-1]
                        r.append(p)
                r.append(1)
                res.append(r)
        return res
a = generate(5)
print(a)
def minimumTotal(triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # [
        #         [2],
        #         [3,4],
        #         [6,5,7],
        #         [4,1,8,3]
        # ]
        #
        # def myMini(n):
        #         if n==1:
        #                 t = triangle[0][0]
        #                 return [t]
        #         else:
        #                 r = triangle[n-1]
        #                 pre = myMini(n-1)
        #                 res = []
        #                 for i in range(n):
        #                         start = 0 if i<1 else i-1
        #                         end = n-2 if i>n-2 else i
        #                         temp = r[i]+pre[start]
        #                         for j in range(start,end+1):
        #                                 x = r[i]+pre[j]
        #                                 if temp>x:
        #                                         temp = x
        #                         res.append(temp)
        #                 return res
        # if len(triangle)==0:
        #         return 0
        # res = myMini(len(triangle))
        # t = res[0]
        # for x in res:
        #         if t>x:
        #                 t = x
        # return t
        length = len(triangle)
        res = [0]
        for row in range(length):
                r = triangle[row] #cur row
                tempRes = [res[0]+r[0]]
                for x in range(1,row):
                        m = min(res[x],res[x-1])+r[x]
                        tempRes.append(m)
                tempRes.append(res[-1]+r[-1])
                res = tempRes

        t = res[0]
        for x in res:
                if t>x:
                        t = x
        return t

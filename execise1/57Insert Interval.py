def insert(intervals, newInterval):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # intervals.append(newInterval)
        # temp = sorted(intervals,key = lambda k:k.start)
        # res = []
        # for x in temp:
        #     if res and x.start<=res[-1].end:
        #         res[-1].end = max(res[-1].end,x.end)
        #     else:
        #         res.append(x)
        # return res
        
        # intervals.append(newInterval)
        # temp = sorted(intervals,key = lambda k:k.start)
        # res = []
        # for x in temp:
        #     if res:
        #         last = res[-1]
        #         if x.start<=last.end:
        #             if last.end<x.end:
        #                 res[-1].end = x.end
        #         else:
        #             res.append(x)
        #     else:
        #         res.append(x)
        # return res
        
        res = []
        for x in intervals:
            if x.start>newInterval.end or x.end <newInterval.start:
                res.append(x)
                i+=1
            else:
                 newInterval = Interval(
                    min(x.start,newInterval.start),
                    max(x.end,newInterval.end)
                )
        res.append(newInterval)
        return sorted(res,key = lambda k:k.start)

a = insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[[4,9]])
print(a)
    

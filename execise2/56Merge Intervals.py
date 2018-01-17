def merge(intervals):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #先按区间起点排序，sorted(intervals,key=lambda k:k.start) 然后遍历即可

a = merge([[1,3],[2,6],[8,10],[15,18]])
print(a)
    

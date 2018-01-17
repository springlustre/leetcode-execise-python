def uniquePaths(m,n):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        v = [1 for _ in range(m)]

        for i in range(1,n):
            for j in range(1,m):
                v[j] = v[j]+v[j-1]
        return v[m-1]



a = uniquePaths(5,4)
print(a)
    

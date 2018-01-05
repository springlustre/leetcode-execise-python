def minPathSum(grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        v = [0 for _ in range(n)]
        for i in range(n):
            v[i] = grid[0][i]+v[i-1]
        # print(v)
        for row in grid[1:]:
            v[0] = row[0]+v[0]
            # print(v)
            for i in range(1,n):
                v[i] = min(v[i-1],v[i])+row[i]
        return v[n-1]



a = minPathSum([[1,2],[5,6],[1,1]])
print(a)
    
